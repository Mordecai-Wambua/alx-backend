import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const client = createClient();

client
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

const getAsync = promisify(client.get).bind(client);

let reservationEnabled = true;
const queue = kue.createQueue();

const app = express();
const port = 1245;

function reserveSeat(number) {
  return client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  return parseInt(await getAsync('available_seats'), 10);
}

app.get('/available_seats', async (req, res) => {
  const available_seats = await getCurrentAvailableSeats();
  return res.json({ numberOfAvailableSeats: available_seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      return res.json({ status: 'Reservation in process' });
    } else {
      return res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();
    if (seats <= 0) {
      reservationEnabled = false;
      return done(Error('Not enough seats available'));
    }
    reserveSeat(seats - 1);
    done();
  });
});

app.listen(port, () => {
  console.log(`Server running. listening at port: ${port}`);
  reserveSeat(50);
});
