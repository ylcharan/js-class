// Demonstrate Destructuring, Spread Operator, Modules

const student = { name: "Charan", regNo: 12300920, city: "Vizag" };
const { name, regNo, city } = student;

const arr = ["red", "blue", "green"];
const [red, blue] = arr;
console.log(red, blue);

const arr1 = [...arr, "lowda", "erripuk"];
console.log(arr1);

const user = { name: "Charan", age: 21 };
const details = { country: "India", college: "LPU" };
const merged = { ...user, ...details };
console.log(merged);
