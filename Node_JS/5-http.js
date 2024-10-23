// creating small HTTP server
const http = require('http');
const fs = require('fs').promises;

// create function countStudents
async function countStudents(path) {
    // read file
    try {
            const data = await fs.readFile(path, 'utf-8')

            // Split data into lines and filter empty line
            const lines = data.split('\n').filter(line => line.trim());

            // Skip header line, get student data
            const students = lines.slice(1);

            if (students.length === 0) {
                return 'Number of students: 0';
            }
    
            let output = `Number of students: ${students.length}`;

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
                output += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`;
            }

            return output;
        } catch (error) {
            throw new Error('Cannot load the database');
        };
}

// http server
const app = http.createServer(async (req, res) => {
    // checking request URL path
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('Hello Holberton School!');
        res.end();
    // checking requested url path
    } else if (req.url === '/students') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write('This is the list of our students:');

        const databasePath = process.argv[2];

        if (!databasePath) {
            res.write('No database provided\n');
            res.end();
            return;
        }

        try {
            const studentData = await countStudents(databasePath);
            res.write(studentData);
        } catch (error) {
            res.write('Cannot load the database');
        }
        res.end();
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.write('Not Found');
        res.end();
    }
}).listen(1245);

// module exporting
module.exports = { app, countStudents };