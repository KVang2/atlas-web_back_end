export default function appendToEachArrayValue(array, appendString) {
  for (const value in array) {
    value = appendString + value;
  }

  return array;
}
