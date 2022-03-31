#!/usr/bin/env bash
set -e

if [[ -z "$SOFIE_USER" ]]
then
  echo "Il faut définir l'utilisateur de SOFIE en utilisant la variable SOFIE_USER"
  exit -1
fi
if [[ -z "$SOFIE_PASSWORD" ]]
then
  echo "Il faut définir le mot de passe de l'utilisateur de SOFIE en utilisant la variable SOFIE_PASSWORD"
  exit -2
fi
if [[ -z "$RECIPIENT_PATTERN" ]]
then
  echo "Il faut définir la liste des destinataires en utilisant la variable RECIPIENT_PATTERN"
  exit -3
fi

FILE="$1"
if [[ -z "$FILE" ||  ! -a "$FILE" ]]
then
  [[ -z $FILE ]] || echo "Un paramètre doit être passé à la commande spécifiant le fichier à uploader."
  [[ -a $FILE ]] || echo "Le fichier passé en paramètre doit exister."
  exit -4
fi

rm -f sofie-cookie.txt || true
# Authentification
echo "Authentification..."
curl 'https://sofie.finances.gouv.fr/linshare/j_security_check' -X POST --compressed \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'WWW-No-Authenticate: linshare' \
  --data-urlencode "login=${SOFIE_USER}" \
  --data-urlencode "password=${SOFIE_PASSWORD}" \
  -c sofie-cookie.txt

# Récupération du token de la page de partage
echo "Récupération du token de partage..."
FORM_DATA=$(curl -s 'https://sofie.finances.gouv.fr/linshare/fr/files/upload' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --compressed -b sofie-cookie.txt  | grep -E -o '<div class="t-invisible"><input value="([^\"]*)" name="t:formdata" type="hidden">' | sed 's/<div class="t-invisible"><input value="\([^\"]*\)" name="t:formdata" type="hidden">/\1/')

# Upload du fichier et récupération de son id
echo "Upload du fichier..."
RESPONSE=$(curl -f -s 'https://sofie.finances.gouv.fr/linshare/webservice/fineuploader/upload/receiver' \
  -X POST -H 'Accept: */*' --compressed \
  -H 'WWW-No-Authenticate: linshare' \
  -H 'Content-Type: multipart/form-data' \
  -F qqfile=@${FILE} \
  -b sofie-cookie.txt)
#{"success":true,"newUuid":"42c5b7c1-7bd3-4704-8f16-91319851ff17","error":null,"async":true,"frequence":5,"filename":"requirements-dev.txt"}

# echo "$RESPONSE"
FILE_UUID=$(echo $RESPONSE | jq -r .newUuid)
FREQUENCE=$(echo $RESPONSE | jq -r .frequence)
ASYNC=$(echo $RESPONSE | jq -r .async)

echo "Gestion de l'upload asynchrone..."
if [[ "$ASYNC" == "true" ]]
then
  sleep ${FREQUENCE}s
  RESPONSE=$(curl -f -X GET -s "https://sofie.finances.gouv.fr/linshare/webservice/fineuploader/upload/receiver/${FILE_UUID}" \
    -H 'Accept: */*' --compressed \
    -H 'WWW-No-Authenticate: linshare' \
    -H 'Content-Type: multipart/form-data' \
    -b sofie-cookie.txt)
  echo "Process asynchrone : attente de complétion..."
  while [[ "$(echo $RESPONSE | jq -r .status )" == "PROCESSING" ]]
  do
    # Attente pour s'assurer que le fichier est bien enregistré dans SOFIE
    sleep ${FREQUENCE}s
    RESPONSE=$(curl -X GET -s "https://sofie.finances.gouv.fr/linshare/webservice/fineuploader/upload/receiver/${FILE_UUID}" \
      -H 'Accept: */*' --compressed \
      -H 'WWW-No-Authenticate: linshare' \
      -H 'Content-Type: multipart/form-data' \
      -b sofie-cookie.txt)
  done
  if [[ $(echo $RESPONSE | jq -r .status ) != "SUCCESS" ]]
  then
    echo "Impossible d'uploader le fichier"
    exit -5
  fi
fi
# echo $RESPONSE
# Récupération de l'UUID de la ressource sauvegardé par SOFIE
FILE_UUID=$(echo $RESPONSE | jq -r .resourceUuid)
# Envoi du partage
echo "Envoi du mail de partage..."
curl -f 'https://sofie.finances.gouv.fr/linshare/fr/files/upload.uploaderform' -X POST --compressed \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'WWW-No-Authenticate: linshare' \
  -b sofie-cookie.txt \
  --data-urlencode 't%3Aformdata='${FORM_DATA} \
  --data-urlencode 't%3Asubmit=submitShare' \
  --data-urlencode "uuids=${FILE_UUID}" \
  --data-urlencode 'is_submit=1' \
  --data-urlencode 'progress=0' \
  --data-urlencode 'recipientsPattern='${RECIPIENT_PATTERN} \
  --data-urlencode 'mailingLists-values=' \
  --data-urlencode 'shareExpiryDate='$(date +%d)'/'$(date +%m)'/'$(date +%Y) \
  --data-urlencode 'secureSharing=on' \
  --data-urlencode 'notificationDate='$(date -d '+2 days' +%d)'/'$(date -d '+2 days' +%m)'/'$(date -d '+2 days' +%Y) \
  --data-urlencode 'textAreaShareNote=' \
  --data-urlencode 'textAreaSubjectValue=' \
  --data-urlencode 'textAreaValue=' \
  --data-urlencode 'submitShare=Envoyer'