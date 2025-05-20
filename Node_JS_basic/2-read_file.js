const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, 'utf8');

    const lines = content.split('\n').filter(line => line.trim() !== '');
    const students = lines.slice(1); // remove header

    const fields = {};
    let total = 0;

    for (const line of students) {
      const parts = line.split(',');
      if (parts.length < 4) continue;

      const firstname = parts[0];
      const field = parts[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
      total++;
    }

    console.log(`Number of students: ${total}`);
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
