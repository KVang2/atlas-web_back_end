export default class Building {
  // Constructor attributes
  constructor(sqft) {
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined || this.evacuationWarningMessage === null) {
      throw new Error('Class extending BUilding must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }
}
