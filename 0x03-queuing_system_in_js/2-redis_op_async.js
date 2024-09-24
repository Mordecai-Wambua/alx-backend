import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

client
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const val = await getAsync(schoolName);
    console.log(val);
  } catch (err) {
    console.error(err);
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
