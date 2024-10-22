const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe ('sendPaymentRequestToAPI', function() {
    it("Test spy SUM method", function() {
        // spy on Utils.calculateNumber
        const spy = sinon.spy(Utils, 'calculateNumber');

        // Define the arguments
        const totalAmount = 100;
        const totalShipping = 20;

        // calling paymentrequest
        sendPaymentRequestToApi(totalAmount, totalShipping);

        // call sinon once then call with others
        sinon.assert.calledOnce(spy);
        sinon.assert.calledWith(spy, 'SUM', totalAmount, totalShipping);

        // restore after spying
        spy.restore();
    });
});