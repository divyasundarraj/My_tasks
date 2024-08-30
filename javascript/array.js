// let fruits = ["apple","banana","cherry"]
// console.log(fruits[0]) 
// console.log(fruits[1]) 
// console.log(fruits[2]) 
//---------------------------------------------------------------------------------------------------------------

//Accessing elements if the mixed array

// let mixed_array = ["apple", 42, true, { name:"divya", age:22}, function() { return "hello"; }];

// console.log(mixed_array[0]);
// console.log(mixed_array[1]);
// console.log(mixed_array[2]);
// console.log(mixed_array[3].name);
// console.log(mixed_array[4]());

//-----------------------------------------------------------------------------------------------------------

//Nested array with mixed data type
//Accessing elemnts of the nested array

// let nested_array = [1, "two", ["three", 4], { key: "value"}]
// console.log("")
// console.log(nested_array[2][0]);
// console.log(nested_array[3].key);

//------------------------------------------------------------------------------------------------------------
//Array properties and methods

// Array replace method

// let fruits = ["apple","banana","cherry"]
// fruits[1] = "Mango";
// console.log(fruits)

//------------------------------------------------------------------

//length property:

//  let fruits = ["apple","banana","cherry","orange"]
//  console.log(fruits.length)

// it returns the length of the array.

//-------------------------------------------------------------------------

// Push mehtod:

// let fruits = ["apple","banana","cherry","orange"]
// fruits.push("Mango")
// console.log(fruits)

// to Add the element at the end.

//---------------------------------------------------------------------------------------------------

// pop method:

// let fruits = ["apple","banana","cherry","orange"]
// fruits.pop()
// console.log(fruits)

// to remove the last element

//-----------------------------------------------------------------------------------------------------

// Shift method:

// let fruits = ["apple","banana","cherry","orange"]
// fruits.shift()
// console.log(fruits)

// to remove the first element

//----------------------------------------------------------------------------------------------------

// Unshift method:

// let fruits = ["apple","banana","cherry","orange"]
// fruits.unshift("mango")
// console.log(fruits)

// to add one or more element at beggining

//------------------------------------------------------------------------------------------------

// Splice mehtod:

// let fruits = ["apple","banana","cherry","orange"]
// let newfruits = fruits.splice(1,2)
// console.log(newfruits)
// console.log(fruits)

// to remove the 1 and 2 index element.

//-------------------------------------------------------------------------------------------------

// forEach method:

// let fruits = ["apple","banana","cherry","orange"]
// fruits.forEach(
//     function(item,index)
//     {console.log(index,item);});

//----------------------------------------------------------------------------------------------------

// Map method:

// let fruits = ["apple","banana","cherry","orange"]
// let upperfruits = fruits.map(function(item)
// {return item.toUpperCase();});
// console.log(upperfruits)

//----------------------------------------------------------------------------------------------------

// Filter method:

// let fruits = ["apple","banana","cherry","orange"]
// let filterfruits = fruits.filter(function(item)
// { return item.endsWith("e")})
// console.log(filterfruits)

//-----------------------------------------------------------------------------------------------------

// Reduce method:

// let fruits = ["apple","banana","cherry","orange"]
// let combinefruits = fruits.reduce(function(total,item)
// { return total + " " + item});
// console.log(combinefruits);

//------------------------------------------------------------------------------------------------

// checking if a variable is an array:

// let fruits_1 = ["apple","banana","cherry","orange"]
// let fruits_2 = ("apple","banana","cherry","orange")

// console.log(Array.isArray(fruits_1))
// console.log(Array.isArray(fruits_2))

//--------------------------------------------------------------------------------------------------

// Sorting Array:

// let numbers = [4,3,1,2,5]
// numbers.sort()
// console.log(numbers)

// let fruits = ["banana","cherry","apple","orange"]
// fruits.sort();
// console.log(fruits)

//-----------------------------------------------------------------------------------------------------

// Reversing Array:

// let numbers = [1,2,3,4,5]
// numbers.reverse();
// console.log(numbers)

//--------------------------------------------------------------------------------------------------------

// Array using for loop:

// for(start,stop,index)
// let fruits = ["banana","cherry","apple","orange"]
// for(let i = 0; i<fruits.length; i++){
//     console.log(fruits[i])
// } 

//-------------------------------------------------------------------------------------------------------------

// Array using forEach method:

// let fruits = ["banana","cherry","apple","orange"]
// fruits.forEach(function(fruit,index)
// {console.log(index,fruit)})

//---------------------------------------------------------------------------------------------------------

// Using for...of lopp method:

// let fruits = ["banana","cherry","apple","orange"]
// for(let fruit of fruits){
//     console.log(fruit)
// }

//--------------------------------------------------------------------------------------------------------

// Using for...in loop:

// let fruits = ["banana","cherry","apple","orange"]
// for(let index in fruits){
//     console.log(index,fruits[index])
// }

// Using reduce method

// let numbers = [1,2,3,4,5]
// let sum = numbers.reduce(function(total,number)
// { return total + number;});
// console.log(sum)

// Using Some method

let numbers = [1,2,3,4,5]
let negative = numbers.some(function(number)
{ return number > 0;})
console.log(negative)



















//---------------------------------------------------------------------








































