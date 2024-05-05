export default function appendToEachArrayValue(array, appendString) {
  for (let [temp, value] of array.entries()) {
    array[temp] = appendString + value;
  }

  return array;
}
