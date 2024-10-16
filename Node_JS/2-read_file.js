// create function countStudents

const fs = require('fs');

function countStudents(path);
    try {
        const data = fs.readFileSync(path, 'utf-8');
        const lines = data.split('\n').filter(line => line.trim());
        const students = lines.slice(1);

        console.log(`Number of students: ${students.length}`);
        const fields = {};

        students.forEach((line))
        }
    } catch (error) {
        console.error('Cannot load the database');
    }
}
