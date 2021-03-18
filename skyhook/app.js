const express = require('express');
const bodyParser = require('body-parser');

// Change values after || to change config for non-docker use
const port = process.env.SKYHOOK_PORT || 3000;
const uploadUri = process.env.SKYHOOK_UPLOAD_URI || '/api/data_providers/upload_data'

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post(uploadUri, (request, response) => {
  const body = request.body;
  const dataSlice = body.data.slice(0, 3);
  const bodyCopy = {...body, data: `[${body.data.length} records]`}

  console.log('============================================')
  console.group('Received data from', body.providerName)
  console.log('request body:', bodyCopy);
  console.log('first three elements of data:', dataSlice);
  console.groupEnd();
  console.log('============================================')

  response.send({message: 'success'})
})

app.listen(port);
console.log(`Listening at http://localhost:${port}`);
