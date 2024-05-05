export default function appendToEachArrayValue(array, appendString) {
  const index = [];
  for (const value of array) {
    index.ppush(appendString + value);
  }
  return index;
}
