process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
  process.exit(); // Forzamos el cierre aquí para que se imprima el mensaje final
});

process.on('exit', () => {
  console.log('This important software is now closing');
});
