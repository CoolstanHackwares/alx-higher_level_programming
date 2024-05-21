#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.log('Please provide a URL as an argument.');
  process.exit(1);
}

request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
