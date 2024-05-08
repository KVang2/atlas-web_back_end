export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
    if (!getListStudents || typeof city !== 'string' || !Array.isArray(newGrades)) {
        return [];
    }

    const studentsInCity = getListStudents().filter((student) => student.location === city);

    const updatedStudents = studentsInCity.map(student => {
        const newGrade = newGrades.find

    })
}