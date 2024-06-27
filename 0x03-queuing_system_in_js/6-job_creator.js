import kue from 'kue';
const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Create a Kue queue with the Redis client
const queue = kue.createQueue('push_notification_code', {
  redis: {
    createClientFactory: function() {
      return client;
    }
  }
});

// Create an object containing the Job data
const object_jobdata = {
  phoneNumber: '12345',
  message: 'This is a test message'
};

// Create a job with the object created before
const job = queue.create('message', object_jobdata).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`)
    job.on('complete', () => {
      console.log('Notification job completed');
    });
  } else {
    console.log(`Notification job failed`)
  }
});
