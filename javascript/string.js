// string literal
let Str1 = "Divya Sundarraj.";
console.log(Str1)

// string object(using new keyword)
let Str2 = new String("Divya");
console.log(Str2)

//chaAt() -----> Retuns the charecter at a specified index.
let str = "Hello";
console.log(str.charAt(0));

//charCodeAt()------> Returns the unicode of the character at a specified index.
let string = "Hello";
console.log(string.charCodeAt(0));

//concat()------->jons two or more strings.
let string1 = "Hello";
let string2 = "World";
console.log(string1.concat(", ",string2));

//includes()----->checks a string contains a specified value,returning true or false.
let str1 = "hello, World";
console.log(str1.includes("World"));

//indexof()----->returns the index of the first accurance of the specified value or -1 if not found.
let str2 = "hello, World";
console.log(str1.indexOf("World"));

//lastindexof()----->returns the index of the last accurance of the specified value or -1 if not found.
let Str = "hello,World";
console.log(Str.lastIndexOf("World"));

//Replace()-----> replaces the specified value with another value n a string.
let Strin = "hello,World";
console.log(Strin.replace("World", "javascript"))

//slice()-----> Extracts a pat of a string and returns it as a new string.
let a = "hello, world";
console.log(a.slice(0,5))

//split()------> splits a string into an array of substring.
let b = "hello, world";
console.log(b.split(", "));

//substring()------> Extracts character from a string between two specified indices.
let c = "hello, world";
console.log(c.substring(7, 12));

//to uppercase---->  converts a string to uppercase letters.
let strupper = "hello, world";
console.log(strupper.toUpperCase());

//to lowerrcase---->  converts a string to lowercase letters.
let strlower = "hello, world";
console.log(strlower.toLowerCase());

//trim()---->remove the whitespaces from both side of a string.
console.log(strlower.trim());

//startwith()---->checks if a string start with a specified value.
console.log(strlower.startsWith("hello"));
console.log(strlower.startsWith("world"));

//endswith()------>checks if a string ends with a specified value.
console.log(strlower.endsWith("world"));
console.log(strlower.endsWith("hello"));

//repeat()------>returns a new string with a specified number copies of the original string.
let repeatstr = "Hello ";
console.log(repeatstr.repeat(3));

//valueof()------>returns the primitve value of a string object.
let valstr = new String("hello, world");
console.log(valstr.valueOf());

//template literals
//string interpolation
// let name = "divya";
// let greeting = "Hello, ${name}"
// console.log(greeting)

//embeded expression--------->validate javascript expression inside a template literal.
let num1 = 5;
let num2 = 10;
let result = 'the sum of '+num1+" and "+num2+" is "+(num1+num2)
console.log(result)

//using template literals with functions.
function greet(name1){
    return "Hello "+name1+ " Welcome to the site.";
}
console.log(greet("Divya"))

//





