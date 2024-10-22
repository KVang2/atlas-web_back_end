// Index page
const assert = require('assert');
const app = require('./api');
const request = require('supertest');

describe ('Index page', () => {
    it('return 200 status code', function(done) {
        request(app)
        .get('/')
        .expect(200)
        .end(function(err, res) {
            if (err)
                return done(err);
            done();
        });
    });

    it('check for correct message', function(done) {
        request(app)
        .get('/')
        .end(function(err, res) {
            if (err)
                return done(err);
            assert.strictEqual(res.text, 'Welcome to the payment system');
            done();
        });
    });
});