import Building from './5-building';

export default class SkyHighBuilding extends Building {
  // Constructor attributes
  constructor(sqft, floors) {
      super(sqft);
      this._sqft = sqft;
      this._floors = floors;
    }

  // Getters
  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
