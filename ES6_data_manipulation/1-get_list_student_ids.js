export default function getListStudentIds(arrayOfStudentsId) {
  if (!Array.isArray(arrayOfStudentsId)) {
    return [];
  }
  return arrayOfStudentsId.map((student) => student.id);
}
