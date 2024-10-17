const express = require('express')

// create express app
const app = express();

app.get('/', (req, res) => {
    res.status(200).send('Hello Holberton School!');
});

// Start server and listen port
app.listen(1245, () => {
    console.log('listening port')
});

module.exports = app;