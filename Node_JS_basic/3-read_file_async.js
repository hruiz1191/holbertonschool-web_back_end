const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1); // remove header

      const fields = {};
      let total = 0;

      for (const line of students) {
        const parts = line.split(',');
        if (parts.length < 4) {
          continue; // eslint-disable-line no-continue
        }

        const firstname = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
        total += 1; // Changed from total++ to satisfy no-plusplus
      }

      console.log(`Number of students: ${total}`);
      for (const [field, names] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve(); // Everything went fine
    });
  });
}

module.exports = countStudents;
