class HolbertonCourse {
  constructor(name, length, students) {
      this._name = typeof name === 'string' ? name : '';
      this._length = typeof length === 'number' ? length : 0;
      this._student = Array.isArray(students) ? students : [];
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
