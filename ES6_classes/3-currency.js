export default class Currency {
        constructor(code, name) {
            if (typeof code !== 'string' || code.trim().length === 0) {
            throw new Error('non empty string');
            }
            if (typeof name !== 'string' || name.trim().length === 0) {
                throw new Error('non empty string');
            }

      this._code = code;
      this._name = name;
    }

    // Getter and setter for code
    get code() {
        return this._code;
    }
    set code(newCode) {
        if (typeof newCode !== 'string' || newCode.trim().length === 0) {
            throw new Error('non empty string');
        }
        this._code = newCode;
      }

    // Getter and setter for name
    get name() {
      return this._name;
    }

    set name(newName) {
      if (typeof newName !== 'string' || newName.trim().length === 0) {
        throw new Error('Name must be a non empty string');
  }
  this._name = newName;
}

displayFullCurrency() {
    return(`${this._name} (${this._code})`);
  }
}
