const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe ("calculateNumber", function () {

    it("Should return 7", function() {
        assert.strictEqual(calculateNumber(2.7, 3.9), 7);
    });

    it('Should return 5', function() {
        assert.strictEqual(calculateNumber(1.2, 4.3), 5)
    });

    it('Should return -10', function() {
        assert.strictEqual(calculateNumber(-5.2, -5.3), -10);
    });
});