function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs) === false) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach((item) => {
    const job = queue.create('push_notification_code_3', item).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    job.on('progress', () => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
