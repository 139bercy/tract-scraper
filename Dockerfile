FROM python:3.9

RUN apt-get clean
RUN apt-get update
RUN apt-get install -y locales
RUN sed -i -e '/fr_FR.UTF-8/s/^# //g' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales

ENV LC_ALL fr_FR.UTF-8

WORKDIR /home/bercy/track-scraper/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /home/bercy/track-scraper/

ENV PYTHONPATH "${PYTHONPATH}:."
ENV PYTHONUNBUFFERED 1
ENV DOCKERIZED true
ENV SCRAPY_SETTINGS_MODULE 'scraper.settings'

CMD ["python", "src/main.py"]
