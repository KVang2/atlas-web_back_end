export default function getStudentsByLocation(getListStudents, city) {
    const students = getListStudents();

  if (!Array.isArray(getListStudents) || students.length === 0 || typeof city !== 'string' || city.trim() === '') {
   return [];   
  }

  return students.filter((student) => student.holbertonClass.location === city);
}
