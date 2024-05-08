export default function cleanSet(set, startstring) {
  if ((startString === '' || typeof startString !== 'string') {
    throw new Error('Invalid arguments');
  }
      const filteredValues = Array.from(set).filter(element => element.startsWith(startString));
      return filteredValues.map(element => element.slice(startString.length)).join('-');
}
