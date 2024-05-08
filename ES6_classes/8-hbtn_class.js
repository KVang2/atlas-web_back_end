export default class HolbertonCLass {
    // Constructor attributes
    constructor(size, location) {
        this._size = size;
        this._location = location;
    }

    // Getter methods
    get size() {
        return this._size;
    }

    get location() {
        return this._location;
    }

    // Conversion methods
    valueOf() {
        return this._size;
    }

    toString() {
        return this._location;
    }
}
