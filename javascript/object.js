// let movie = {
//     name:"Ghilli",
//     directer:"suriya",
//     producer:"sri surya",
//     displayInfo:function(){
//         console.log(movie.name+" was directed by "+movie.directer)
//     }
// }
// movie.displayInfo()

//object constructor dunction

// const myFather = new Person("divya","priya",20,"blue")
// const myMother = new Person("divya","priya",20,"blue")
// function Person(first,last,age,eye)
// {
//     this.firstname = first;
//     this.lastname = last;
//     this.age = age;
//     this.eyeColor = eye;

// }
// Person.prototype.nationality = "english";

// console.log(myFather.nationality)


// const folder1 = {
//     firstname:"Divya",
//     lastname:"S",
//     age:50,
//     height:150
// }
// const folder2 = {firstname:"priya",lastname:"G"}
// Object.assign(folder1,folder2)
// let result = Object.entries(folder1)
// console.log(result)
//syntax-----> object.assign(target,source)

let obj = {};
Object.defineProperty(obj,"property",{
    value:42,
    num:34,
    writable:true
})
console.log(obj.property)
obj.property = 100;
console.log(obj.property)
obj.property = 20;
console.log(obj.property)
//syntax-----> object.defineProperty(object,property,descriptor)





















