// Index page
const assert = require('assert');
const request = require('request');

const base = 'http://localhost:7865';

describe ('Index page', () => {
    it('return 200 status code', function(done) {
        request.get(base, (error, response, body) => {
            if (error)
                return done(error);
            assert.strictEqual(response.statusCode, 200);
            done();
        });
    });

    it('check for correct message', function(done) {
        request.get(base, (error, response, body) => {
            if (error)
                return done(error);
            assert.strictEqual(body, 'Welcome to the payment system');
            done();
        });
    });

    it('Return correct content-type', (done) => {
        request.get(base, (error, response, body) => {
            if (error)
                return done(error);
            assert.strictEqual(response.headers['content-type'], 'text/html; charset=utf-8');
            done();
        });
    });
});