export default class HolbertonCourse {
  constructor(name, length, students) {
    // Verify name is a string
      if (typeof name !== 'string' || name.trim().length === 0) {
        throw new TypeError('Name must be non-empty string');
      }

      // Verify length is a number
      if (typeof length !== 'number' || length <= 0) {
        throw new TypeError('Length be positive number');
      }

    // Verify length is a number
    if (!Array.isArray(students) || !students.every(student => typeof student === 'string' || student.trim().length === 0)) {
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
  if (typeof newName !== 'string' || newName.trim().length === 0) {
    throw new Error('Name must be non-empty');
  }
  this._name = newName;
}

// Getter and setter for length attri
get length() {
  return this._length;
}
set length(newLength) {
  if (typeof newLength === 'number' && newLength > 0) {
      this._length = newLength;
  }
}

// Getter and setter for students attri
get students() {
  return this._students;
}
set students(newStudents) {
  if (Array.isArray(newStudents) && newStudents.every(student => typeof student === 'string' && student.trim().length > 0)) {
      this._students = newStudents;
  } else {
        throw new TypeError('Students must be non-empty array of strings');
    }
  }
}