// creating small HTTP server
const http = require('http');
const fs = require('fs').promises;
const path = require('path');


const app = http.createServer((req, res) => {
    // checking request URL path
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('Hello Holberton School!');
        res.end();
} else {
    // checking requested url path
    if (req.url === '/students') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('This is the list of our students');
        res.end();
    }
}).listen(1245);


module.exports = app;