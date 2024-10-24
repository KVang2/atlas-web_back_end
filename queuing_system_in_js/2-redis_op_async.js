// using promisify
import { promisify } from 'util';
const fs = require('fs');
const readFileAsync = promisify(fs.readFile);

// redis-client.js
import { createClient, print } from 'redis';

// create redis client
const client = createClient();

// Client connect handling
client.on('connect', () => {
    console.log('Redis client connected to the server')
});

// error handling
client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

// function set for school
function setNewSchool(schoolName, value, callback) {
    client.set(schoolName, value, print)
    if (callback) callback();
}

// function set displaySchoolvalue
function displaySchoolValue(schoolName, callback) {
    client.get(schoolName, (error, reply) => {
        if (error) {
            console.log(`Error on value for key ${schoolName}: ${error.message}`);
        } else {
            console.log(`${reply}`);
        }
        if (callback) callback();
    });
}

// Connecting to Redis
client.connect().then(() => {
    displaySchoolValue('Holberton', () => {
        setNewSchool('HolbertonSanFrancisco', '100', () => {
            displaySchoolValue('HolbertonSanFrancisco', () => {
                client.quit();
            });
        });
    });
});