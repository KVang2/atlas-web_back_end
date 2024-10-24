// redis-client.js
import { createClient } from 'redis';

// create redis client
const client = createClient();

// function set for school
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

// function set displaySchoolvalue
function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, reply) => {
        if (error) {
            console.log(`Error on value for key ${schoolName}: ${error.message}`);
        } else {
            console.log(`Value for ${schoolName}: ${reply}`);
        }
    });
}

// Client connect handling
client.on('connect', () => {
    console.log('Redis client connected to the server');

    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
});

// error handling
client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

// Connecting to Redis
client.connect();