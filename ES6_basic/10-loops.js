export default function appendToEachArrayValue(array, appendString) {
  const index = [];
  for (const value of array) {
    index.push(appendString + value);
  }
  return index;
}
