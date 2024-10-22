const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

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

describe("test suit for stub", function() {
    it("Stub methods", function() {
        const stub = sinon.stub(Utils, 'calculateNumber');

        stub.withArgs('SUM', 10, 20).returns(100);

        stub.returns(10);

        sendPaymentRequestToApi(100, 20);

        sinon.assert.calledOnce(stub);
        sinon.assert.calledWith(stub, 'SUM', 100, 20);

        stub.restore();
    });
});