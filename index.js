const pm = require('@postman/postman-sdk');

pm.initialize({
    collectionId: process.env.COLLECTION_UID,
    apiKey: process.env.API_KEY,
    debug: true,
    truncateData: true,
});

const express = require('express');
const app = express();
const bodyParser = require("body-parser");
const serveStatic = require("serve-static");

app.use(bodyParser.json());
//app.use(serveStatic("public"));

app.get('/', (req, res) => {
  const name = process.env.NAME || 'World';
  res.status(500).json({response: "ko", desc: "Root Access. Pleaase check the doc online"});
    });

app.get('/locate/:ip', (req, res) => {
    var ip = req.params.ip;
    res.status(200).json({response: "ok", desc: "Locate a public IP", IP: ip});
   });

app.get('/details/:countryCode', (req, res) => {
    var countryCode = req.params.countryCode;
    res.status(200).json({response: "ok", desc: "Get details about a countryCode", countryCode: countryCode});
   });

app.get('/chatgpt/:city', (req, res) => {
    var city = req.params.city;
    res.status(200).json({response: "ok", desc: "Get a short sentence about a city (AI generated)", city: city});
   });

app.get('/explore/:city', (req, res) => {
    var city = req.params.city;
    res.status(200).json({response: "ok", desc: "Explore the world with the city of your choice", city: city});
   });

const port = parseInt(process.env.PORT) || 8080;
app.listen(port, () => {
  console.log(`helloworld: listening on port ${port}`);
});