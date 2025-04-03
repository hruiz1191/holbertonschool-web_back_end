export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }
  // crea la memoria
  const buffer = new ArrayBuffer(length);
  // crea una vista manipulable
  const view = new DataView(buffer);
  // coloca el valor en la posición
  view.setInt8(position, value);

  return view;
}
