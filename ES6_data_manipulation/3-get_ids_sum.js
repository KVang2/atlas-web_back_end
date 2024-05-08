export default function getStudentIdsSum(getListStudents) {
  const students = getListStudents();

  if (!Array.isArray(students)) {
      return 0;
  }

  const reducer = (sum, student) => sum + student.id;
  return students.reduce(reducer, 0);
}
