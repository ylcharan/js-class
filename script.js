// const num = [1, 2, 3, 4, 5];

// const evens = num.filter((e) => e % 2 == 0);

// const sum = evens.map((prev, cur) => prev + cur);

// console.log(sum[sum.length - 1]);

// const num1 = [10, 25, 45, 60, 70, -1];
// const val = 45;

// console.log(num1.indexOf(val));
// console.log(num1.indexOf(60));

// let isPositive = true;
// for (const n of num1) {
//   if (n < 0) {
//     isPositive = false;
//   }
// }

// console.log(isPositive ? "All are positive" : "contains negative int."); // turnery operator

// const students = [
//   { name: "x", mark: 95 },
//   { name: "y", mark: 75 },
//   { name: "z", mark: 88 },
//   { name: "a", mark: 45 },
// ];

// const failed = students.filter((e) => e.mark <= 45);
// const average = students.map((prev, curr) => (prev.mark + curr.mark) / 2);

// const totalScore = students.reduce((current, std) => current + std.mark, 0);
// console.log(`average marks : ${totalScore}`);

// const [x, y, z = 100] = [1, 2];
// console.log(x, y, z);

// const arr1 = [1, 2, 3];
// const arr2 = [4, 5];

// console.log([...arr2, ...arr1]); // spread operator

// function sum(...nums) { // function name(...args) {}
//   return nums.reduce((total, n) => total + n);
// }

// console.log(sum(1, 3, 4, 5, 6));

// const numbers = [10, 20, 30, 40];
// const [a, b] = numbers;

// console.log(a, b); // 10 20

// const [x, , y, z = 100] = [1, 2, 3];
// console.log(x, y, z); // 1 3 100

// const person = { name: "Alice", age: 25, country: "India" };
// const { name, age } = person;

// console.log(name);

const colors = ["Red", "Green", "Blue"];
const [first, ...second] = colors;

console.log(first, second);

const person = { name: "Alice", age: 25, city: "Delhi" };
person.age = 20;
console.log(person.age);

const nums = [10, 20, 30];
const [fistEl, , restEl] = nums;
console.log(fistEl, restEl);

const car = { brand: "Tesla" };
const { brand: carBrand, model = "Model S" } = car;
console.log(carBrand, model);

const user = { id: 1, info: { firstName: "John", lastName: "Doe" } };

const {
  id,
  info,
  info: { lastName, firstName },
} = user;

console.log(id, info, lastName, firstName);

function sum(...args) {
  return args.reduce((acc, cur) => acc + cur);
}

console.log(sum(1, 2, 3, 4));

const student = { name: "Manjot", age: 22, course: "CSE", city: "Ludhiana" };
const { name, age, ...rest } = student;
console.log(name, age, rest);

const fruits = ["apple", "banana", "cherry", "date"];
const [a, b, ...res] = fruits;
