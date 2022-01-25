from pathlib import Path
import re

def path_leaf(path):
    if isinstance(path, str):
        path = path.split('?')[0]
    return Path(path).name.strip()

def clean_url(url):
    url = re.sub(r"\/?page\/\d+", "",  url)

    if not url.endswith('/'):
        url = f"{url}/"
    
    return url
