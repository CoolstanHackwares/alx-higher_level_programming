#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Please provide both the file path and content as arguments.');
  process.exit(1);
}

fs.writeFile(filePath, content, (err) => {
  if (err) {
    console.error(`Error writing file: ${err.message}`);
  }
});
