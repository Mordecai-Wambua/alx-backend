import kue from 'kue';
import { expect } from 'chai';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('jobs not an array', () => {
    expect(() => createPushNotificationsJobs(43, queue)).to.throw(
      'Jobs is not an array'
    );
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(
      'Jobs is not an array'
    );
    expect(() => createPushNotificationsJobs('Testing', queue)).to.throw(
      'Jobs is not an array'
    );
  });
});
