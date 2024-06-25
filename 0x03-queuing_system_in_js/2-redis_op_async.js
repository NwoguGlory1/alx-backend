import redis from 'redis';
import { promisify } from 'util';

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

// promisify callback function, client.GET
// also bind it afterwards
const getAsync = promisify(client.GET).bind(client);

// we can now use async/await 
// in the now async function
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(`${value}`);
  } catch (error) {
    console.error(` ${error.message}`);
  }
 }

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
