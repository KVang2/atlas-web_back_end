export default class Building {
  // Constructor attributes
  constructor(sqft) {
    if (typeof sqft !== 'number' || sqft < 0) {
      throw new Error('Error sqft must be a positive number');
    }
      this._sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
      return this._sqft;
    }
  // Method to be overridden by subclasses
  evacuationWarningMessage() {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
}