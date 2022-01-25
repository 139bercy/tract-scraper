# Getting started

Create a virtual environment:

```
python3 -m venv venv
```

Activate it:

```
. venv/scripts/activate
```

Install the program requirements:

```
pip install -r requirements.txt
```

Export the environment variable SCRAPY_SETTINGS_MODULE:

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

Depending on the number of websites to scrap, the process should not even take a minute.

All the downloaded tracts will be find in the ***downloads*** folder at the end of the process.