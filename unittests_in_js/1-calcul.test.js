const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe ("calculateNumber", function() {

    it("if sum should return sum of 6", function() {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it("if sum should return sum of 6", function() {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it("if SUBTRACTION should return 8", function() {
        assert.strictEqual(calculateNumber('SUBTRACT', 18, 10), 8);
    });

    it("if DIVIDE should return 2", function() {
        assert.strictEqual(calculateNumber('DIVIDE', 10, 5), 2);
    });

    it("if Divide b = 0 return error", function() {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
});