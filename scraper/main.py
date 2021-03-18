import requests
import json
import os

# Change values after 'or' to change config for non-docker use
filePath = os.getenv('SCRAPER_DATA_FILE_PATH') or 'MOCK_DATA.json'
skyhookHost = os.getenv('SKYHOOK_HOST') or 'localhost'
skyhookPort = os.getenv('SKYHOOK_PORT') or '3000'
skyhookUploadUri = os.getenv('SKYHOOK_UPLOAD_URI') or '/api/data_providers/upload_data'
skyhookUrl = f'http://{skyhookHost}:{skyhookPort}{skyhookUploadUri}'

with open("MOCK_DATA.json", "r") as data_file:
    scraped_data = json.loads(data_file.read())

data = json.dumps(
    {
        "providerName": "movieForumScraper",
        "batchName": "movieForumScraper 14-7-2020 16:80 lorem ipsum",
        "data": scraped_data
    }
).encode("utf-8")

response = requests.post(skyhookUrl, data=data, headers={"Content-Type": "application/json"})
print(json.loads(response.content))
