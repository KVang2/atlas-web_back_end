const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe ('sendPaymentRequestToAPI', function() {
    let consoleSpy;

    beforeEach(function() {
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        consoleSpy.restore();
        sinon.restore();
    });

    it("call Utils.calculate 'Sum', 100, 20", function() {
        // Define the arguments
        const totalAmount = 100;
        const totalShipping = 20;
        
        // calling paymentrequest
        sendPaymentRequestToApi(totalAmount, totalShipping);
        
        // call sinon once then call with others
        sinon.assert.calledOnce(consoleSpy);
        sinon.assert.calledWith(consoleSpy, 'The total is: 120'); 
    });

    it("call Utils.calculate 'Sum', 100, 20", function() {
        // Define the arguments
        const totalAmount = 10;
        const totalShipping = 10;

        // calling paymentrequest
        sendPaymentRequestToApi(totalAmount, totalShipping);

        // call sinon once then call with others
        sinon.assert.calledOnce(consoleSpy);
        sinon.assert.calledWith(consoleSpy, 'The total is: 20'); 
    });
});