import os
import requests
import urllib.request
from bs4 import BeautifulSoup

def download(page_url):

    os.makedirs("download", exist_ok=True)

    print("Getting download url...")
    soup = BeautifulSoup(requests.get(page_url).text, "html.parser")
    data_url = soup.find("button", {"id": "detail-download-button"}).get("data-url")
    filename = (
        soup.find("h2", class_="title").text.lower()
        .replace("information about ", "")
        .replace(" ", "-")
        .replace(".", "-")
        + ".exe"
    )
    download_url = "https://dw.uptodown.net/dwn/" + data_url + filename
    
    print("Downloading file...")
    response = requests.get(download_url, stream=True, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code == 200:
        with open(f"download/{filename}", "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Download complete: {filename}")
    else:
        print(f"Failed to download. Status code: {response.status_code}")