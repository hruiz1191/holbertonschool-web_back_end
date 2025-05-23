const http = require('http');
const fs = require('fs');

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const fields = {};
    let total = 0;

    for (const line of students) {
      const parts = line.split(',');
      if (parts.length < 4) continue;

      const firstname = parts[0];
      const field = parts[3];

      if (!fields[field]) fields[field] = [];
      fields[field].push(firstname);
      total += 1;
    }

    let result = `Number of students: ${total}\n`;
    for (const [field, names] of Object.entries(fields)) {
      result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    resolve(result.trim());
  });
});

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    if (!database) {
      res.end('This is the list of our students\nCannot load the database');
      return;
    }

    countStudents(database)
      .then((data) => {
        res.end(`This is the list of our students\n${data}`);
      })
      .catch(() => {
        res.statusCode = 500;
        res.end('This is the list of our students\nCannot load the database');
      });
    return;
  }

  res.statusCode = 404;
  res.end('Not Found');
});

app.listen(1245);

module.exports = app;
