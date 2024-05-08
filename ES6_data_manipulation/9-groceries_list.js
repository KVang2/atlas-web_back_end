export default funtion groceriesList() {
  // Creating a new Map to store groceries
  const groceryMap = new Map();

  // Add grocery items (name, quantity) to the map
  groceryMap.set('Apples', 10);
  groceryMap.set('Tomatoes', 10);
  groceryMap.set('Pasta', 1);
  groceryMap.set('Rice', 1);
  groceryMap.set('Banana', 5);

  // Return map
  return groceryMap;
}