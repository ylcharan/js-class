var str1 = "Lakshmi";
var str2 = "Charan";

console.log(Array.from(str1));

let list = [1, 2, 3, 4, 5, 2, 5];

let li = new Set(list);
console.log(Array.from(li));

let numbers = Array.from([1, 2, 3, 4], (x) => x > 2);
console.log(numbers);

let arrayLen = Array.from({ length: 5 }, (_, i) => i + 1);
console.log(arrayLen);
