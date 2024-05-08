export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students) || students.length === 0 || typeof city !== 'string' || city.trim() === '') {
   return [];   
  }

  return students.filter(student => student.holbertonClass.location === city);
}
