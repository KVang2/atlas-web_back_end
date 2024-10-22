// creating the Utils module
const Utils = {};

Utils.calculateNumber = function(type, a, b) {
    if (type === 'SUM') {
        return Math.round(a) + Math.round(b);
    }

    if (type === 'SUBTRACT') {
        return Math.round(a) - Math.round(b);
    }

    if (type === 'DIVIDE') {
        const rA = Math.round(a);
        const rB = Math.round(b);
        if (rB === 0) {
            return "Error";
        }
        return rA / rB;
    }
};

// exporting utils module
module.exports = Utils;