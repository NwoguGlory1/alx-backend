import kue from 'kue';
const queue = kue.createQueue();

// Create an object containing the Job data
const object_jobdata = {
  phoneNumber: '12345',
  message: 'This is a test message'
};

const queueName = 'push_notification_code';

// Create a job with the object created before
const job = queue.create(queueName, object_jobdata).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
});
job.on('complete', () => {
    console.log('Notification job completed');
  });

job.on('failed', () => {
    console.log(`Notification job failed`)
});
