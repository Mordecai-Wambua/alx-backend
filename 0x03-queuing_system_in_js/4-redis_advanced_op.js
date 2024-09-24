import { createClient, print } from 'redis';

const client = createClient();

client
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

const hashfields = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};
for (const [k, v] of Object.entries(hashfields)) {
  client.hset('HolbertonSchools', k, v, print);
}
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error(err);
  }
  if (reply !== null) {
    console.log(reply);
  }
});
