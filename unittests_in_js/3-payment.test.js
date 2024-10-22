const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe ('sendPaymentRequestToAPI', function() {
    it("Test spy SUM method", function() {
        const spy = sinon.spy(Utils, 'calculateNumber');

        const totalAmount = 100;
        const totalShipping = 20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        sinon.assert.calledOnce(spy);
        sinon.assert.calledWith(spy, 'SUM', totalAmount, totalShipping);

        spy.restore();
    });
});