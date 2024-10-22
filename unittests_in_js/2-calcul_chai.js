// new argument type (sum, subtract, or divide)
function calculateNumber(type, a, b) {
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
}

module.exports = calculateNumber;