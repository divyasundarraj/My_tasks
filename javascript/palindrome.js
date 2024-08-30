let str = "malayalam";
let reversedStr = str.split("").reverse().join("");
console.log(reversedStr);
if(str==reversedStr){
    console.log("The given string is palindrome")
}
else{
    console.log("The given string is not palindrome")
}