export default class Building {
  // Constructor attributes
  constructor(sqft) {
    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== ' function') {
      throw new Error('Class extending BUilding must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Method to be overridden by subclasses
  evacuationWarningMessage() {
    throw new Error('evacuationWarningMessage must be implemented by subclass');
  }
}
