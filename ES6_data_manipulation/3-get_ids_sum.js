export default function getStudentIdsSum(getListStudents) {
  const students = getListStudents();
    
  // Check if students is an array
  if (!Array.isArray(students)) {
    return 0;
  }

  // Use reduce to calculate the sum of student IDs
  const reducer = (sum, student) => sum + student.id;
  return students.reduce(reducer, 0);
}
  