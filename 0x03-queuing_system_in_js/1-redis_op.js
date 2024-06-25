import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value){
  client.SET(schoolName, value, (err, result)=> {
    redis.print(`Set value for key ${schoolName} to ${value}`);
  });
}

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, value) => {
    console.log('Get value for key ${schoolName}: ${value}`);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
