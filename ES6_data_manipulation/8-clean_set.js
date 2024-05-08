export default function cleanSet(startstring) {
  if (!(set instanceof Set) || startString !== 'string') {
    throw new Error('Invalid arguments');
}   

let result = '';
set.forEach((value) => {
  if (typeof value === 'string' && value.startsWith(startString)) {
    if (startString === '' {
        result += value + '-';
    } else {
        const restOfString = value.substring(startString.length);
        result += startString + restOfString + '-';
    }
  }
});

  if (result.endsWith('-')) {
    result = result.slice(0, -1);
  }

return result;
}
