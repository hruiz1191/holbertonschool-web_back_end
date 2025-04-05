export default function cleanSet(set, startString) {
  if (!startString || !set || !(set instanceof Set)) {
    return '';
  }

  const filtered = Array.from(set)
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  return filtered.join('-');
}
