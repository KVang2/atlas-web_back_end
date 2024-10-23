// create function countStudents
const fs = require('fs');

function countStudents(path) {
    try {
        // Read CSV file
        const data = fs.readFileSync(path, 'utf-8');

        // Split data into lines and filter empty line
        const lines = data.split('\n').filter(line => line.trim());

        // Skip header line, get student data
        const students = lines.slice(1);

        if (students.length === 0) {
            console.log('Number of students: 0');
            return;
        }
    
        console.log(`Number of students: ${students.length}`);

        // store students by their field
        const fields = {};

        // process each student entry
        students.forEach((student) => {
            const [firstname, lastname, age, field] = student.split(',');

            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        });

        for (const field in fields) {
            const studentList = fields[field];
            console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;