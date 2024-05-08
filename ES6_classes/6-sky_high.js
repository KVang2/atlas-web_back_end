import Building from './5-building';

export default class SkyHighBuilding extends Building {
  // Constructor attributes
  constructor(sqft, floors) {
      super(sqft);
      this._floors = floors;
      this._sqft = sqft;
    }

  // Getters
  get floors() {
    return this._floors;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
