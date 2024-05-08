export default function getStudentIdsSum(getListStudents) {
  const students = getListStudents();

  if (!Array.isArray(getListStudents)) {
      return 0;
  }

  return students.reduce((sum, student) => sum + student.id, 0);
}
