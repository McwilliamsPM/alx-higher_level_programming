#!/usr/bin/node
const count = process.argv.length;
if (count <= 3) {
  console.log('0');
} else {
  const args = process.argv.map(Number).slice(2, count).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
