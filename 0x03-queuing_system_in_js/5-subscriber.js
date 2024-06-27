import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Step 2: Subscribe to the channel
const channel = 'holberton school channel';
client.subscribe(channel);

// Step 3: Handle incoming messages
client.on('message', (channel, message) => {
  console.log(`Received message from ${channel}: ${message}`);

// Step 4: Graceful shutdown on receiving 'KILL_SERVER'
if (message === 'KILL_SERVER') {
    client.unsubscribe(channel, () => {
    client.quit();
  });
}
