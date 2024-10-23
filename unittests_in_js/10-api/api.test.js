// Endpoints

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

// Cart Page
describe('Cart page', () => {
    it('correct status code (200) when id is a num', function(done) {
        request.get(`${base}/cart/123`, (error, response, body) => {
            if (error)
                return done(error);
            assert.strictEqual(response.statusCode, 200);
            assert.strictEqual(body, 'Payment methods for cart 123');
            done();
        });
    });

    it('return 404 for invalid id', function(done) {
        request.get(`${base}/cart/invalidId`, (error, response, body) => {
            if (error)
                return done(error);
            assert.strictEqual(response.statusCode, 404);
            done();
        });
    });
});

// payments
describe ('login page and payments', () => {
    it('return 200 status code', function(done) {
        request.get('http://localhost:7865/available_payments', (error, response, body) => {
            const paymentResponse = {
                payment_methods: {
                    credit_cards: true,
                    paypal: false
                }
            };
            if (error)
                return done(error);
            assert.strictEqual(response.statusCode, 200);
            assert.deepStrictEqual(JSON.parse(body), paymentResponse);
            done();
        });
    });
});