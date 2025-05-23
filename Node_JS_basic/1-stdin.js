process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\r\n`);  // Usamos \r\n para Windows
  process.exit();  // Forzamos la salida después de escribir el nombre
});

process.on('exit', () => {
  process.stdout.write('This important software is now closing\n');
});
