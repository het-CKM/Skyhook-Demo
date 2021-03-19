const axios = require('axios')
const fs = require('fs')

// Change values after || to change config for manual use
const filePath = process.env.CRAWLER_DATA_FILE_PATH || 'MOCK_DATA.json'
const skyhookHost = process.env.SKYHOOK_HOST || 'localhost'
const skyhookPort = process.env.SKYHOOK_PORT || '3000'
const skyhookUploadUri = process.env.SKYHOOK_UPLOAD_URI || '/api/data_providers/upload_data'
const skyhookUrl = `http://${skyhookHost}:${skyhookPort}${skyhookUploadUri}`;

const fileContent = fs.readFileSync(filePath);
const crawledData = JSON.parse(fileContent);

const currentTime = new Date().toLocaleString();
const data = {
  providerName: 'proAnaCrawler',
  batchName: `proAnaCrawler ${currentTime}`,
  data: crawledData
};

axios
  .post(skyhookUrl, data)
  .then(response => console.log(response.data))
  .catch(reason => console.error(reason.message));
