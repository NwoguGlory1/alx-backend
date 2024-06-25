import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a value for a key
function setNewSchool(schoolName, value){
  client.SET(schoolName, value, redis.print );
}

// Function to get the value of a key, log it to console
function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, value) => {
    console.log(`${value}`);
  });
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
