// redis-client.js
import { createClient } from 'redis';

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

// Connecting to Redis
client.connect();