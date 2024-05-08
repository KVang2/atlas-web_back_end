export default function updateUniqueItems(groceryMap) {
  if (!(groceryMap instanceof Map)) {
      throw new Error('Cannot be process');
  }
  groceryMap.forEach((val, key) => {
      if (val === 1) {
          groceryMap.set(key, 100);
      }
  });
  return groceryMap;
}
