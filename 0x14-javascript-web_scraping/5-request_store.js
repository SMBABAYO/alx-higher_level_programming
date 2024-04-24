#!/usr/bin/node

const fs = require('fs');

// Import the 'request' module
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
