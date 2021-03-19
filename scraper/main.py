from datetime import datetime
import requests
import json
import os

# Change values after 'or' to change config for manual use
filePath = os.getenv('SCRAPER_DATA_FILE_PATH') or 'MOCK_DATA.json'
skyhookHost = os.getenv('SKYHOOK_HOST') or 'localhost'
skyhookPort = os.getenv('SKYHOOK_PORT') or '3000'
skyhookUploadUri = os.getenv('SKYHOOK_UPLOAD_URI') or '/api/data_providers/upload_data'
skyhookUrl = f'http://{skyhookHost}:{skyhookPort}{skyhookUploadUri}'

with open(filePath, "r") as data_file:
    scraped_data = json.loads(data_file.read())

currentTime = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')

data = json.dumps(
    {
        "providerName": "movieForumScraper",
        "batchName": f"movieForumScraper {currentTime} lorem ipsum",
        "data": scraped_data
    }
).encode("utf-8")

try:
    response = requests.post(skyhookUrl, data=data, headers={"Content-Type": "application/json"})
    response.raise_for_status()
    print(json.loads(response.content))
except requests.exceptions.HTTPError as exception:
    print(exception)
except requests.exceptions.ConnectionError as exception:
    print("failed to connect to host with url: " + skyhookUrl)
    print(exception)
except requests.exceptions.RequestException as exception:
    print("request to host failed with url: " + skyhookUrl)
    print(exception)
