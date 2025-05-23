const express = require('express');
const fs = require('fs');

const app = express();

// Student count function (same as previous exercise)
const countStudents = (path) => new Promise((resolve, reject) => {
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
      if (parts.length < 4) continue; // eslint-disable-line no-continue

      const firstname = parts[0];
      const field = parts[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
      total += 1;
    }

    let result = `Number of students: ${total}\n`;
    for (const [field, names] of Object.entries(fields)) {
      result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    resolve(result.slice(0, -1)); // Remove last newline
  });
});

// Routes
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const database = process.argv[2];

  if (!database) {
    res.send('This is the list of our students\nCannot load the database');
    return;
  }

  try {
    const studentData = await countStudents(database);
    res.send(`This is the list of our students\n${studentData}`);
  } catch (error) {
    res.send('This is the list of our students\nCannot load the database');
  }
});

app.listen(1245);

module.exports = app;
