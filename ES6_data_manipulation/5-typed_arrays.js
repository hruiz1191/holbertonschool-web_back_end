export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length); // crea la memoria
  const view = new DataView(buffer);      // crea una vista manipulable

  view.setInt8(position, value);          // coloca el valor en la posición

  return view;
}
