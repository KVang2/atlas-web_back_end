const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe ("calculateNumber", function() {

    it("if sum should return sum of 6", function() {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.be.equal(6);
    });

    it("if SUBTRACTION should return 8", function() {
        expect(calculateNumber('SUBTRACT', 18, 10)).to.be.equal(8);
    });

    it("if DIVIDE should return 2", function() {
        expect(calculateNumber('DIVIDE', 10, 5)).to.be.equal(2);
    });

    it("if Divide b = 0 return error", function() {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.be.equal('Error');
    });
});