export default class HolbertonCourse {
  constructor(name, length, students) {
    // Verify name is a string
      if (typeof name !== 'string') {
        throw new TypeError('Name must be non-empty string');
      }

      // Verify length is a number
      if (typeof length !== 'number') {
        throw new TypeError('Length be positive number');
      }

    // Verify length is a number
    if (!Array.isArray(students) || !students.every(student => typeof student)) === 'string')) {
        throw new TypeError('Students must be an non-empty array of strings');
    }

    // Store attributes with underscore
    this._name = name;
    this._length = length;
    this._students = students;
  }

// Getter and setter for name attribute
get name() {
  return this._name;
}
set name(newName) {
  if (typeof newName === 'string') {
      this._name = newName;
  }
}

// Getter and setter for length attri
get length() {
  return this._length;
}
set length(newLength) {
  if (typeof newLength === 'number') {
      this._length = newLength;
  }
}

// Getter and setter for students attri
get students() {
  return this._students;
}
set students(newStudents) {
  if (Array.isArray(newStudents)) {
      this._students = newStudents;
    }
  }
}
