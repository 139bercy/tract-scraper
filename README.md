# Installation and execution

After cloning the project, *cd* in the project directory and execute the following command lines.

## In a local environment

Create a virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment:

```
. venv/scripts/activate
```

Install the program requirements:

```
pip install -r requirements.txt
```

Export the environment variable *SCRAPY_SETTINGS_MODULE*:

```
export SCRAPY_SETTINGS_MODULE='scraper.settings'
```

Create two folders respecting the following treeview:

```
src/scraper/downloads
src/scraper/archives
```
Execute the application:

```
python3 src/main.py
```

## In a Docker environment

You can also deployed the application using ***Docker*** by simply running the code line:
```
docker-compose up
```

# Settings

The application can be configured via some variables available in the *settings.py* file located in the directory :

```
src/scraper/
```

The application can scrap articles and files from months back. This number of months can be configured using the *MONTHS_TO_SCRAP* variable.
```
MONTHS_TO_SCRAP = 1
```

The downloaded content can be archived during a certain period of time (expressed in months) which can be set in the MONTHS_TO_ARCHIVE variable.

```
MONTHS_TO_ARCHIVE = 3
```

In addition to scraping some HTML content, the application can also download some files which extensions can be filtered in the *EXT_TO_SCRAP* variable.

```
EXT_TO_SCRAP = [".pdf", ".doc", ".docx"]
```





# Results
Depending on the number of websites to scrap, the process should not even take a minute.

At the end of the process, all the downloaded files will be find in the ***downloads*** folder.

When the application is deployed, the CI pipeline is in charge to automatically move the files from the ***downloads*** folder to the ***archives*** folder before each run.

In a local environment, these files have to be moved manually in the ***archives*** folder.

