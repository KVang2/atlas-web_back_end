export default function groceriesList() {
  // Creating a new Map to store groceries
  const groceryItem = new Map();

  // Add grocery items (name, quantity) to the map
  groceryItem.set('Apples', 10);
  groceryItem.set('Tomatoes', 10);
  groceryItem.set('Pasta', 1);
  groceryItem.set('Rice', 1);
  groceryItem.set('Banana', 5);

  // Return map
  return groceryItem;
}