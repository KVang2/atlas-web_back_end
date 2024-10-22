const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe ('getPaymentTokenFromAPI', function() {
    it('test for async code using done', function(done) {
        getPaymentTokenFromAPI(true).then((result) => {
            expect(result).to.deep.equal({ data: 'Successful response from the API' });
            // signal test is complete
            done();

        // Ensure errors are handle
        }).catch(done);
    });
});