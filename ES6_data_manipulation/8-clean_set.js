export default function cleanSet(startstring) {
  if (!(set instanceof Set) || startString !== 'string') {
    throw new Error('Invalid arguments');
}   

let result = '';
set.forEach((value) => {
  if (value.startsWith(startString)) {
    result += `${value.substring(strartString.length)}-`;
  }
});

  if (result.endsWith('-')) {
    result = result.slice(0, -1);
  }

return result;
}
