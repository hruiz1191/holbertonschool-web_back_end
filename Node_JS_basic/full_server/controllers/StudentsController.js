import { readDatabase } from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const database = process.argv[2] || 'database.csv';

    try {
      const fields = await readDatabase(database);
      let response = 'This is the list of our students\n';

      Object.keys(fields).sort().forEach((field) => {
        response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      });

      res.status(200).send(response.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const database = process.argv[2] || 'database.csv';
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const fields = await readDatabase(database);
      res.status(200).send(`List: ${fields[major].join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
