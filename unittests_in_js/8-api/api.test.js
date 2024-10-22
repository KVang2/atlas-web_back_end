// Index page
const assert = require('assert');
const app = require('./api');
const request = require('supertest');

describe ('Index page', () => {
    it('return 200 status code', function(done) {
        request(app)
        .get('/')
        .end(function(err, res) {
            if (err)
                return done(err);
            assert.strictEqual(res.status, 200);
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

    it('Return correct content-type', (done) => {
        request(app)
        .get('/')
        .end(function(err, res) {
            if (err)
                return done(err);
            assert.strictEqual(res.headers['content-type'], 'text/html; charset=utf-8');
            done();
        });
    });
});