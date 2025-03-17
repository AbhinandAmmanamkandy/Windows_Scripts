import os
import requests
import urllib.request
from bs4 import BeautifulSoup

# Get latest release version number
def get_version(url):
    response = requests.get(url + "/releases/latest", allow_redirects=True)
    soup = BeautifulSoup(response.text, "html.parser")
    meta_tag = soup.find("meta", attrs={"name": "apple-itunes-app"})
    return meta_tag["content"].split("/")[-1]

# Get all released apk links
def get_links(url, zip):
    response = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(response.text, "html.parser")
    return [f"https://github.com{a.get("href")}" for a in soup.find_all("a", href=True) if a["href"].endswith(".zip" if zip else ".apk")]

# Basic download
def download_file(link, name, folder="download"):
    os.makedirs(folder, exist_ok=True)  
    urllib.request.urlretrieve(link, f"{folder}/{name}")

# Ask the user which to download
def get_latest_release(url, zip=False):
    version = get_version(url)

    url = f"{url}/releases/expanded_assets/{version}"
    print(url)
    file_links = get_links(url, zip)
    names = [link.split('/')[-1] for link in file_links]

    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

    choice = int(input("Enter choice: ")) - 1
    download_file(file_links[choice], names[choice])