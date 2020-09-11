
// forEach 
// forEach iterates over an array, runs a callback on
// each value and returns undefined

// Using the For Each function

function forEach(arr, callback) {
    for (var i = 0; i<arr.length; i++) {
        callback(arr[i], i, arr);
    }
}


// Example of For Each

function halfValues(arr) {
    var newArr = [];
    arr.forEach(function(val) {
        newArr.push(val/2);
    });
    return newArr;
}









//  Using the findIndex function 

function findIndex(arr, callback){
    for (var i = 0; i<arr.length; i++) {
        if (callback(arr[i], i, arr)) {
            return i;
        }
    }
    return -1;
}

function callback(curElement, curIndex, array) {
    // call back implemented by caller of function
}

// Example
var arr = [3,4,6,2,1];
findIndex(arr, function(num, index, array) {
    return num === 6;
});
// Result: 2    which is the index of when num === 6







setTimeout(function(){}, amount_of_time)
setInterval(function(){}, amount_of_intervals)

function countDown(seconds) {
    var intervalId = setInterval(function() {
        seconds--;
        if (seconds > 0) {
            console.log("Timer: ", seconds);
        } else {
            console.log("Ring Ring Ring!!!");
            clearInterval(intervalId);
        }
    }, 1000);
} 








// Example of how to use a button for a request
//  Practice website can be  jsonplaceholder.typicode.com

var btn = document.querySelector("button");
var section = document.querySelector("#comments");
btn.addEventListener("click", sendRequest);

function sendRequest() {
    axios.get("https://someWebsiteAPI.com", {
        params: {
            postID: 1,
            etc : "other param"
        }
    })
    .then(addComments)
    .catch(handleErrors)
}

function addComments(res){
    res.data.forEach(function(comment) {
        appendComment(comment);
    });
}

// Some appendComment function here

function handleErrors(err) {
    if (err.response) {
        console.log("Problem with Response ", err.response.status);
    } else if (err.request) {
        console.log("Problem with Request!");
    } else {
        console.log("Error", err.message);
    }
}







// map
// map creates a new array, runs a callback on
// each value and pushes the result of each callback
// in the new array of equal length



// map function example  -- map always returns an array of the same length.

var arr = [1,2,3];

arr.map(function(value, index, array) {
    return value * 2;
});

// [2,4,6]

function map(arr, callback) {
    var newArr = [];
    for(var i = 0; i < arr.length; i++) {
        newArr.push(callback(arr[i], i, arr))
    };
    return newArr;
}

// Example using map in a function

function tripleValues(arr) {
    return arr.map(function(value) {
        return value * 3;
    });
}







// filter
// filter creates a new array, runs a callback on
// each value and if it the rsult of the callback returns
// true, that value is added to the new array



// Example using FILTER function

var arr = [1,2,3];

arr.filter(function(value, index, array) {
    return value > 2;
})
//  will return [3]



function filter(arr, callback) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (callback(arr[i], i, arr)) {
            newArr.push(arr[i]);
        }
    }
    return newArr;
}

// Example using filter in a function

function onlyFourLetterNames(arr) {
    return arr.filter(function(value) {
        return value.length === 4;
    });
}






// some
// some iterates through an array and runs a callback
// on each value, if the callback for at least one value 
// returns true, some returns true, otherwise false



//  Example using SOME function

var arr = [1,2,3];

arr.some(function(value, index, array) {
    return value < 2;
});
//  Will return:   true


function some(arr, callback) {
    for (var i = 0; i < arr.length; i++) {
        if (callback(arr[i], i, arr)) {
            return true;
        }
    }
    return false;
}

//  Example using some in a function

function hasEvenNumber(arr) {
    return arr.some(function(value) {
        return value % 2 === 0;
    });
}

function hasComma(str) {
    return str.split('').some(function(value) {
        return value === ',';
        });
}








// every
// every iterates through an array and runs a callback
// on each value, if the callback at any time returns
// false, every returns false


//  Example using EVERY function

var arr = [1,2,3];
arr.every(function(value, index, array) {
    return value < 0;
});
// will return: true


function every(arr, callback) {
    for (var i = 0; i < arr.length; i++) {
        if (callback(arr[i], i, arr) === false ) {
            return false;
        }
    }
    return true;
}

//  Example using every in a function

function allLowerCase(str) {
    return str.split('').every(function(value) {
        return value === value.toLowerCase();
    });
}

function allArrays(arr) {
    return arr.every(Array.isArray);
}



//  reduce
// reduce returns an accumulated value which is 
// determined by the result of what is returned
//  to each callback 



//  Example using REDUCE function

var arr = [1,2,3,4,5];

arr.reduce(function(accumulator, nextValue, index, array) {
    return accumulator + nextValue;
}, optionalSecondParameter);


var names = ['Tim', 'Matt', 'Colt', 'Elie'];

names.reduce(function(accumulator, nextValue) {
    return accumulator += " " + nextValue;
}, 'The instructors are');


var arr = [5,4,1,4,5];

arr.reduce(function(accumulator, nextValue){
    if (nextValue in accumulator) {
        accumulator[nextValue]++;
    } else {
        accumulator[nextValue] = 1;
    }
    return accumulator;
}, {});

// Using reduce in a function

function sumOddNumbers(arr) {
    return arr.reduce(function(accumulator, nextValue) {
        if (nextValue % 2 !==0) {
            accumulator += nextValue;
        }
        return accumulator;
    }, 0);
}

function createFullName(arr) {
    return arr.reduce(function(accumulator, nextValue) {
        accumulator.push(nextValue.first + " " + nextValue.last);
        return accumulator;
    }, []);
}










//  call

// We can use call in the example below to make our code
// run as expected
var person = {
    firstName: "Colt", 
    sayHi : function() {
        return "Hi " + this.firstName;
    }, 
    determineContext: function() {
        return this === person;
    },
    dog : {
        sayHello: function() {
            return "Hello " + this.firstName;
        },
        determineContext: function() {
            return this === person;
        }
    }
}

person.dog.sayHello.call(person); // "Hello Colt"
person.dog.determineContext.call(person); // true
// Notice we do NOT invoke sayHello or determineContext with
// parenthesis after. We use call as the function



// Here is another example of how call simplifies our code
function sayHi() {
    return "Hi " + this.firstName;
}

var colt = {
    firstName: "Colt"
}

var elie = {
    firstName: "Elie"
}

sayHi.call(colt); // Hi Colt
sayHi.call(elie); // Hi Elie




// Example 3 of using call

var divs = document.getElementsByTagName('div ');

// How can we find all the divs that the text "hello". 
// Using filter would be ideal, but divs is not an array
divs.filter // undefined

// so we can convert our array-like-object into an array
var divsArray = [].slice.call(divs);
// Then use filter on the new divsArray variable
divsArray.filter(function(val) {
    return val.innerText === 'hello';
});










// apply

// The big difference between call and apply 
// is the amount of parameters

function addNumbers(a,b,c,d) {
    return this.firstName + " just calculated " + (a+b+c+d);
}

var colt = {
    firstName: "Colt"
}

var elie = {
    firstName: "Elie"
}

// we can use call like this:
addNumbers.call(elie,1,2,3,4) // Elie just calculated 10
// we can use apply like this:
addNumbers.apply(elie, [1,2,3,4]) // Elie just calculated 10

// When to use apply?
// When a function does not accept an array, apply will
// spread out the values in an array for us!

var nums = [5,7,1,4,2];

Math.max(nums); // NaN    since max doesnt accept an array input

// so we can use apply
Math.max.apply(this, nums); // 7



// Another example:
function sumValues(a,b,c) {
    return a + b + c;
}

var values = [4,1,2];

sumValues(values); // "4,1,2undefinedundefined"
// since sumValues does not accept array input

sumValues.apply(this, values); // 7








// bind

// The parameters work like call, but bind returns
// a function with the context of 'this' bound already!

function addNumbers(a,b,c,d) {
    return this.firstName + " just calculated " + (a+b+c+d);
}


var elie = {
    firstName: "Elie"
}

// In the below example, the keyword 'this'
// is bound to the first parameter
var elieCalc = addNumbers.bind(elie,1,2,3,4); // function(){}...
elieCalc(); // Elie just calculated 10

// We can also use this when perhaps we don't 
// know all of the parameters.
// So, we do NOT need to have all of the parameters
// upfront

var elieCalc = addNumbers.bind(elie,1,2); // function(){}...
elieCalc(3,4); // Elie just calculated 10

// so when using bind, we don't need to know
// all of the parameters, just what we want
// the keyword 'this' to be


// We also use bind for aynchronus code

var colt = {
    firstName: "Colt",
    sayHi: function() {
       setTimeout(function() {
           console.log("Hi " + this.firstName);
       }, 1000);
    }
}

// Since this.firstName is called at a later time, 
// the 'this' keyword will actually refer
// to the window object

colt.sayHi(); // Hi undefined (1000 milliseconds later)

// so we can use bind to help us
var colt = {
    firstName: "Colt",
    sayHi: function() {
       setTimeout(function() {
           console.log("Hi " + this.firstName);
       }.bind(this), 1000);
    }
}

colt.sayHi(); // Hi Colt (1000 milliseconds later)

function invokeMax(fn, num){
    var max = 0;
    
    return function() {
        if (max >= num) return "Maxed Out!";
        max++;
        console.log(this)
        return fn.apply(this,arguments);
    };
    
}





// I think this is bind written out as a function:

function bind(fn, thisArg){
    var outerArgs = [].slice.call(arguments,2)
    return function(){
        var innerArgs = [].slice.call(arguments)
        var allArgs = outerArgs.concat(innerArgs)
        return fn.apply(thisArg, allArgs)
    }
}











// Keyword 'new'

function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
}

var elie = new Person("Elie", "Schoppik");


// Constructor Function

function House(bedrooms, bathrooms, numSqft) {
    this.bedrooms = bedrooms;
    this.bathrooms = bathrooms;
    this.numSqft = numSqft;
}

var firstHouse = House(2,2,1000)
firstHouse // undefined -- why?
// We are not explicitly binding the keyword
// "this" or placing it inside a declared object.

// we have to use the 'new' keyword
var firstHouse = new House(2,2,1000);



// Example

function Dog(name, age) {
    this.name = name;
    this.age = age;
    this.bark = function() {
        console.log(this.name + " just barked!");
    }
}

var rusty = new Dog("Rusty", 7);
var bella = new Dog("Bella", 3);

rusty.bark()
bella.bark()

// Four things the key word "new" does:

// 1) Creates an empty object out of thin air.

// 2) It sets the value of the keyword 'this' in the 
// function which it is being used with to be that 
// empty object that was just created.

// 3) It adds an implict "return this" at the end of the 
// function so that the object created using the 
// "new" keyword can be returned from the function.

// 4) It adds the "__proto__" property to the object
// that was just created.





// Example -- Multiple Constructors

function Car(make,model,year) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.numWheels = 4;
}

function Motorcycle(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.numWheels = 2;
}

// But this code is duplicated, so how can we make it easier?

function Motorcycle(make, model, year) {
    Car.call(this, make, model, year)
    this.numWheels = 2;
}

//  OR

function Motorcycle(make, model, year) {
    Car.apply(this, [make, model, year]);
    this.numWheels = 2;
}

// OR

function Motorcycle() {
    Car.apply(this, arguments);
    this.numWheels = 2;
}








// Prototype
function Person(name) {
    this.name = name;
}

var elie = new Person("Elie");
var colt = new Person("Colt");


elie.__proto__ === Person.prototype; // true
colt.__proto__ === Person.prototype; // true

Person.prototype.constructor === Person; // true


// We can add methods like so:

Person.prototype.isInstructor = true;

elie.isInstructor; // true
colt.isInstructor; // true




//  Example of Refactoring

function Person(name) {
    this.name = name;
    this.sayHi = function() {
        return "Hi " + this.name;
    }
}

elie = new Person("Elie");
elie.sayHi(); // Hi Elie

//  The above is inefficient because every time
//  we create a new object, we would have to 
// redefine the sayHi function

// we can make use of the prototype function as follows:

function Person(name) {
    this.name = name;
}

person.prototype.sayHi = function() {
    return "Hi " + this.name;
}

elie = new Person("Elie");
elie.sayHi(); // Hi Elie



//  Practice Problem

function Vehicle(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year; 
    this.isRunning = false;
}

Vehicle.prototype.turnOn = function() {
    this.isRunning = true
}

Vehicle.prototype.turnOff = function() {
    this.isRunning = false
}

Vehicle.prototype.honk = function() {
    if (this.isRunning) {
        return "beep";
    }
}









// Inheritance


function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
}

person.prototype.sayHi = function() {
    return "Hi " + this.firstName + " " + this.lastName;
}

function Student(firstName, lastName) {
    return Person.apply(this, arguments);
}

Student.prototype.sayHi = function() {
    return "Hi " + this.firstName + " " + this.lastName;
}



// How can we simplify the code above to have some inheritance?

function Student(firstName, lastName) {
    return Person.apply(this, arguments);
}

// We need to set the prototype property
Student.prototype = Object.create(Person.prototype);

Student.prototype.status = function() {
    return "I am currently a student!"
}

var elie = new Person("Elie", "Schoppik");
elie.status // undefinied  -- the property doesnt affect the parent

Student.prototype.constructor; // Person

// need to set the constructor to Student
Student.prototype.constructor = Student;







//  const

// allows us to create constants
var name = 'Brandon';
name = "Felipe";
name // Felipe

const name2 = "Ryan"
name2 = "Brandon" // TypeError -- can't change the variable

const name2 = "Other" // Syntax Error -- can't rewrite the variable



//  Let

// can reassign, but not redeclare
var instructor = "Ellie";
if (instructor === "Ellie") {
    let funFace = "Plays the cello";
}

funFact; // ReferenceError

// let creates a block scope -- so it's only defined
// in the block of code it's in




//  Arrow Functions


var add = function(a,b) {
    return a+b;
}
//  These two functions are the same
var add = (a,b) => a+b;



// Example 2
[1,2,3].map(function(value) {
    return value * 2;
});

// is the same as
[1,2,3].map(value => value * 2);



// Ex 3
function doubleAndFilter(arr) {
    return arr.map(function(value){
        return value * 2;
    }).filter(function(value) {
        return value % 3 === 0;
    })
};

doubleAndFilter([5,10,15,20]); // 30

// is the same as

var doubleAndFilter = arr => arr.map(val => val*2).filter(num => num % 3 === 0);

// arrow functions do not get their own 'this' keyword.
// inside the arrow function, the keyword 'this'
// has its original meaning from the enclosing context


// Ex 4
var instructors = {
    firstName: "Elie",
    sayHi: function(){
        setTimeout(() => {
            console.log(`Hello ${this.firstName}`);
        }, 1000);
    }
}

// We need to use the word function after sayHi
// so the keyword 'this' still refers to the 
// object: instructors


// arrow functions also don't get the keyword: arguments
var add = (a,b) => {
    return arguments;
}

add(2,4); // ReferenceError: arguments is not defined

// but it can be used in an innerfunction, but it'll only
// be applicable to the outer function's arguments



// Default Parameters
function add(a=10,b=20) {
    return a+b;
}


// For .. of loop

var arr = [1,2,3,4,5];

for (let val of arr) {
    console.log(val);
}

// Similar to python for loop

// Can be used on data structures with a Symbol.iterator method
// (so, not objects)






// Rest
function printRest(a,b,...c) {
    console.log(a)
    console.log(b)
    console.log(c)
}

printRest(1,2,3,4,5);
// 1
// 2
// [3,4,5]



// 3 ways to do the same thing:
function sumArguments() {
    var total = 0;
    for(var i =0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}

function sumArguments() {
    var argumentsArray = [].slice.call(arguments);
    return argumentsArray.reduce(function(acc,next) {
        return acc + next;
    });
}


var sumArguments = (...args) => args.reduce((acc, next) => acc + next);





// Spread

// Useful when you have an array, but what you 
// are working with expects comma separated values

// Example 1
// ES5
var arr1 = [1,2,3];
var arr2 = [4,5,6];
var arr3 = [7,8,9];

var combined = arr1.concat(arr2).concat(arr3);

// ES2015
var combined = [...arr1, ...arr2, ...arr3];



// Example 2
var arr = [3,2,4,1,5];
Math.max(arr); // NaN

Math.max.apply(this, arr); // 5

Math.max(...arr); // 5


// Ex 3
function sumValues(a,b,c) {
    return a+b+c;
}

var nums = [12,15,20];

// ES5
sumValues.apply(this, nums); // 47

// ES2015
sumValues(...nums); // 47



// example from exercises:


//                                      condition ? value if true : value if false
function sumEvenArgs(...args){
    return args.reduce((acc, next) => next % 2 === 0 ? acc += next : acc, 0)
  }


  /* 
Write a function called flip which accepts a function and a value for the keyword this. Flip should return a new function that when invoked, will invoke the function passed to flip with the correct value of the keyword this and all of the parameters passed to the function REVERSED. HINT - if you pass more than two parameters to flip, those parameters should be included as parameters to the inner function when it is invoked. You will have to make use of closure!

Examples:

    function personSubtract(a,b,c){
        return this.firstName + " subtracts " + (a-b-c);
    }
    
    var person = {
        firstName: 'Elie'
    }
    
    var flipFn = flip(personSubtract, person);
    flipFn(3,2,1) // "Elie subtracts -4"
    
    var flipFn2 = flip(personSubtract, person, 5,6);
    flipFn2(7,8). // "Elie subtracts -4"

    flip(subtractFourNumbers,this,1)(2,3,4) // -2
    flip(subtractFourNumbers,this,1,2)(3,4) // -2
    flip(subtractFourNumbers,this,1,2,3)(4) // -2
    flip(subtractFourNumbers,this,1,2,3,4)() // -2
    flip(subtractFourNumbers,this)(1,2,3,4) // -2
    flip(subtractFourNumbers,this,1,2,3)(4,5,6,7) // -2
    flip(subtractFourNumbers,this)(1,2,3,4,5,6,7,8,9,10) // -2
    flip(subtractFourNumbers,this,11,12,13,14,15)(1,2,3,4,5,6,7,8,9,10) // -22

*/


function flip(fn, thisArg, ...outerArgs){
    return function(...innerArgs) {
        let allArgs = outerArgs.concat(innerArgs).slice(0, fn.length);
        return fn.apply(thisArg, allArgs.reverse());
    };
}

/* 
Write a function called bind which accepts a function and a value for the keyword this. Bind should return a new function that when invoked, will invoke the function passed to bind with the correct value of the keyword this. HINT - if you pass more than two parameters to bind, those parameters should be included as parameters to the inner function when it is invoked. You will have to make use of closure!

Examples:

    function firstNameFavoriteColor(favoriteColor){
        return this.firstName + "'s favorite color is " + favoriteColor
    }
    
    var person = {
        firstName: 'Elie'
    }
    
    var bindFn = bind(firstNameFavoriteColor, person);
    bindFn('green') // "Elie's favorite color is green"
    
    var bindFn2 = bind(firstNameFavoriteColor, person, 'blue');
    bindFn2('green') // "Elie's favorite color is blue" 
    
    function addFourNumbers(a,b,c,d){
        return a+b+c+d;
    }

    bind(addFourNumbers,this,1)(2,3,4) // 10
    bind(addFourNumbers,this,1,2)(3,4) // 10
    bind(addFourNumbers,this,1,2,3)(4) // 10
    bind(addFourNumbers,this,1,2,3,4)() // 10
    bind(addFourNumbers,this)(1,2,3,4) // 10
    bind(addFourNumbers,this)(1,2,3,4,5,6,7,8,9,10) // 10

*/

function bind(fn, thisArg, ...outerArgs){
    return function(...innerArgs) {
        return fn.apply(thisArg, [...outerArgs, ...innerArgs]);
    };
}








// Object Shorthand

var firstName = "Brandon";
var lastName = 'Redmond';

// ES5 we wrote it like this
var instructor = {
    firstName: firstName,
    lastName: lastName
}

// ES2015 we can write it more simply if the key matches the value
var instructors = {
    firstName, 
    lastName
}

// Object Methods

// ES5
var instructor = {
    sayHello: function() {
        return "Hello!";
    }
}



// ES2015 -- do NOT use arrow functions here!
var instructor = {
    sayHello() {
        return "Hello!";
    }
}




// ES5
var firstName = "Elie";
var instructor = {};
instructor[firstName] = "That's me!"

instructor.Elie; // "That's me!"

// ES2015
var firstName = "Elie";
var instructor = {
    [firstName]: "That's me!"
}

instructor.Elie; // "That's me!"







// Destructuring
// Extracting values from data stored in objects and arrays 

// ES5
var instructor = {
    firstName: "Brandon",
    lastName: "Redmond"
}

var firstName = instructors.firstName;
var lastName = instructors.lastName;

firstName; // "Brandon"
lastName; // "Redmond"



// ES2015
var {firstName, lastName} = instructor;

firstName; // "Brandon"
lastName; // "Redmond"



// below we are giving this function some defualt values that is 
// already a deconstructed object
function createInstructor({name = {first:"Matt", last:"Lane"}, isHilarious = false} = {}) {
    return [name.first, name.last, isHilarious];
}

function displayInfo({name, favColor}) {
    return [name, favColor];
}

var instructor = {
    name: "Brandon",
    favColor: "Purple"
};

displayInfo(instructor); // ['Brandon', 'Purple']




// Array Destructuring


// EX 1

// ES5
var arr = [1,2,3];

var a = arr[0];
var b = arr[1];
var c = arr[2];

// ES2015
var [a,b,c] = arr;


// EX 2

// ES5
function returnNumbers(a,b) {
    return [a,b];
}

var first = returnNumbers(5,10)[0]
var second = returnNumbers(5,10)[1];

// notice that we have to invoke the function twice

// ES2015
[first,second] = returnNumbers(5,10);


// swapping varibales in ES2015
function swap(a,b) {
    return [a,b] = [b,a];
}











//  class

// classes do not HOIST -- so much write them at the top of the script

// ES5
function Student(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
}

var brandon = new Student('Brandon', 'Redmond');


// ES2015
class Student {
    constructor(firstName, lastName) { // this is similar to the __init__ minus the self
        this.firstName = firstName;
        this.lastName = lastName;
    }
}

var brandon = new Student('Brandon', 'Redmond');


// Instance Methods

// ES5

function Student(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
}

Student.prototype.sayHello = function() {
    return "Hello " + this.firstName;
}

// ES2015

class Student {
    constructor(firstName, lastName) { // this is similar to the __init__ minus the self
        this.firstName = firstName;
        this.lastName = lastName;
    }
    sayHello() {
        return `Hello ${this.firstName}`;
    }
}



// Class Methods

class Student {
    constructor(firstName, lastName) { // this is similar to the __init__ minus the self
        this.firstName = firstName;
        this.lastName = lastName;
    }
    sayHello() {
        return `Hello ${this.firstName}`;
    }
    static isStudent(obj) {
        return obj.constructor === Student;
    }
}





// Inheritance

class Person {
    constructor(firstName, lastName){
        this.firstName = firstName;
        this.lastName = lastName;
    }
    sayHello() {
        return `Hello ${this.firstName}`;
    }
}

class Student extends Person {

}






// SUPER

// Super can only be used if a mehtod by the same name is implemeted 
// in the parent class

class Person {
    constructor(firstName, lastName){
        this.firstName = firstName;
        this.lastName = lastName;
    }
    sayHello() {
        return `Hello ${this.firstName}`;
    }
}

class Student extends Person {
    constructor(firstName, lastName) {
        // you must use super here!
        super(firstName, lastName);
    }
}














// SETS

var s = new Set;

// can also be created from an array
var s2 = new Set([3,1,4,1,2,1,5]); // {3,1,4,2,5}

s.add(10); // {10}
s.add(20); // {10, 20}

s.size; // 2

s.has(10); // true

s.delete(20); // true

s.size; // 1









// Promises

// A one time guaranteed return of some future value
// 
// When that value is figure out - the promise is resolved/fulfilled or rejected
// 
// Friendly way to refactor callback code

// Simple Example:
function displayAtRandomTime(){
    return new Promise(function(resolve, reject) {
        setTimeout(function(){
            if(Math.random() > 0.5) {
                resolve('Yes!');
            } else {
                reject('No!');
            }
        }, 1000);
    });
}


// The returned value from a promise will always contain a 
//  .then and .catch method which are functions to be
// executed when the promise is resolved or rejected

displayAtRandomTime().then(function(value) {
    console.log(value);
}).catch(function(error) {
    console.log(error);
});




// Ex 2
var years = [];
$.getJSON('https://omdbapi.com?t=titanic&apikey=thewdb')

.then(function(movie) {
    years.push(movie.Year);
    return $.getJASON('https://omdbapi.com?t=shrek&apikey=thewdb');
})

.then(function(movie) {
    years.push(movie.Year);
    console.log(years);
})

console.log('All Done!');



// Promise.all

// Accepts an array of promises and resolves all of them or
// rejects once a single one of the promises has been first
// rejected (fails fast).

// If all of the passed-in promises fulfull, Promise.all is fulfilled
// with an array of the values from the passed-in promises, in
// the same order as the promises passed in.


function getMovie(title) {
    return $.getJSON(`https://omdbapi.com?t=${title}&apikey=thewdb`);
}

var titanicPromise = getMovie('titanic');
var shrekPromise = getMovie('shrek');
var braveheartPromise = getMovie('braveheart');

// We can now resolve all of the promise using Promise.all

Promise.all([titanicPromise, shrekPromise, braveheartPromise]).then(function(movies) {
    return movies.forEach(function(value) {
        console.log(value.Year);
    });
});



// Promises Assignment

/*1. Write a function called getMostFollowers, which accepts a variable number 
of arguments. You should then make an AJAX call to the Github User 
API (https://developer.github.com/v3/users/#get-a-single-user) to get the 
name and number of followers of each argument. The function should return a 
promise, which when resolved, returns a string which displays the username 
who has the most followers. 

Hint - Try to use Promise.all to solve this and remember that the jQuery 
AJAX methods ($.getJSON, $.ajax, etc.) return a promise.

getMostFollowers('elie','tigarcia','colt').then(function(data){
    console.log(data)
});
 
"Colt has the most followers with 424" 
*/

function getMostFollowers(...usernames) {
    let baseUrl = "https://api.github.com/users";
    let urls = usernames.map(username => $.getJSON(baseUrl + username));
    return Promise.all(urls).then(function(data) {
        let max = data.sort((a,b) => a.followers < b.followers)[0];
        return `${max.name} has the most folowers with ${max.followers}`;
    });
}






/*
2. Write a function called starWarsString, which accepts a number. 
You should then make an AJAX call to the Star Wars 
API (https://swapi.co/ ) to search for a specific character by the 
number passed to the function. Your function should return a promise 
that when resolved will console.log the name of the character.

starWarsString(1).then(function(data){
    console.log(data)
})
 
"Luke Skywalker"
*/

function starWarsString(id) {
    var str = '';
    return $.getJSON(`hhtps://swapi.co/api/people/${id}/`).then(function(data) {
        str += `${data.name} is featured in `;
        let filmData = data.folms[0];
        return $.getJSON(filmData);
    }).then(function(res) {
        str += `${res.title}, directed by ${res.director} `
        let planetData = res.planets[0];
        return $.getJSON(planetData);
    }).then(function(res) {
        str += `and it takes place on ${res.name}`;
        return str;
    }).then(function(finalString) {
        return finalString;
    });
}




// Bonus 1 -  Using the data from the previous AJAX call above, 
// make another AJAX request to get the first film that character is 
// featured in and return a promise that when resolved will console.log 
// the name of the character and the film they are featured in 

// starWarsString(1).then(function(data){
//     console.log(data)
// })
 
// "Luke Skywalker is featured in The Empire Strikes Back, directed by Irvin Kershner"









// Bonus 2 -  Using the data from Bonus 1 - make another AJAX 
// call to get the information about the first planet that the 
// film contains. Your function should return a promise that when 
// resolved will console.log the name of the character and the film 
// they are featured in and the name of the planet. 

// starWarsString(1).then(function(data){
//     console.log(data)
// })
 
// "Luke Skywalker is featured in The Empire Strikes Back, directed by Irvin Kershner and it takes place












// Generators

// we use the * to notate a generator function
function* pauseAndReturnValues(num) {
    for (let i = 0; i < num; i++) {
        yield i;
    }
}

var gen = pauseAndReturnValues(5);

gen.next(); // {value: 0, done: false}
gen.next(); // {value: 1, done: false}
gen.next(); // {value: 2, done: false}
gen.next(); // {value: 3, done: false}
gen.next(); // {value: 4, done: false}
gen.next(); // {value: undefined, done: true}

// OR we can iterate it using a for of loop

for(val of pauseAndReturnValues(3)) {
    console.log(val);
}

// 0
// 1
// 2


// Ex 2 Async Generators

function* getMovieData(movieName) {
    console.log('starting')
    yield $.getJSON(`https://omdbapi.com?t=${movieName}&apikey=thewdb`);
    console.log('ending')
}

var movieGetter = getMovieData('titanic');
movieGetter.next().value.then(val => console.log(val));







// Object & Array Methods

// Object.assign
// creates copies of objects without the same reference!

var o = {name: "Brandon"};
varo2 = Object.assign({}, o); // must put in empty object first!
o2.name =  "Ryan";
o.name; // "Brandon"


// Array.from   converts an Array-like-object into an array

var divs = document.getElementsByTagName("div");
// in this case, divs is an'array-like-object'
var converted = Array.from(divs);
// converted is an array


// find
// invoked on arrays
// Accepts a callback with value, index, and array (just like forEach, map, filter, etc)
// Returns the value found or undefined if not found

var instructors = [{name: 'Brandon'}, {name: 'Felipe'}, {name: "Lee"}, {name: "Lyndsey"}];

instructors.find(function(val) {
    return val.name === 'Lee';
}); // {name: "Lee"}

// findIndex
// Similar to find, but returns an index of -1 if the value is not found
instructors.findIndex(function(val) {
    return val.name === "Lee";
}); // 2


// includes
// returns a boolean if a value is in a string - easier than using indexOf
// ES5
"awesome".indexOf("some") > -1 // true
// ES2015
"awesome".includes('some'); // true


// Number.isFinite
// A handy way for handling NaN being a typeof number
function seeIfNumber(val) {
    if(Number.isFinite(val)) {
        return "It is a number!";
    }
}









// ES2016 & ES2017


// Exponentiation Operator **

// [].includes returns boolean if item in array




// padStart & padEnd
"awesome".padEnd(10, '!'); // awesome!!!




// Async Functions
// a special kind of function that is created using the word async
// The purpose of async functions is to simplify writing
// asynchronous code, specifically Promises

async function first() {
    return "we did it!";
}

first(); // returns a promise

first().then(val => console.log(val)); // "We did it!"

// keyword 'await'
// A reserved keyword that can only be used inside async functions

// await pauses the execution of the async function and is followed 
// by a Promise. The await keyword waits for the promise to resolve, 
// and then resumes the async function's execution and returns the 
// resolved value.

// Think of the await keyword like a pause button (similar to yield
// with generators)


async function getMovieData(movieName) {
    console.log('starting')
    var MovieData = await $.getJSON(`https://omdbapi.com?t=${movieName}&apikey=thewdb`);
    // this line does NOT run until the promise is resolved
    console.log('all done!');
    console.log(movieData);
}

getMovieData() // logs an object with data about the movie!


// Object async
// We can also place async functions as methods inside objects!

var movieCollector = {
    data: "titanic", 
    async getMovie() {
        var response = await $.getJSON(`https://omdbapi.com?t=${this.data}&apikey=thewdb`);
        console.log(response);
    }
}

movieCollector.getMovie();



// Class async

class MovieData {
    constructor(name) {
        this.name = name;
    }
    async getMovie() {
        var response = await $.getJSON(`https://omdbapi.com?t=${this.data}&apikey=thewdb`);
        console.log(response);
    }
}

var m = new MovieData('shrek');
m.getMovie();





// Handling Errors
// If a promise is rejected using await, an error will be thrown
// so we can easily use try/catch statement to handle erros!

async function getUser(user) {
    try{
        var response = await $.getJson(`https://api.github.com/users/${user}`);
        console.log(response.name);
    } catch(e) {
        console.log("User does not exist!");
    }
}


// Thinking about HTTP Requests

// In this example, we are making two requests sequentially
async function getMovieData(movieName) {
    var responeOne = await $.getJSON(`https://omdbapi.com?t=titanic&apikey=thewdb`);
    var responeTwo = await $.getJSON(`https://omdbapi.com?t=shrek&apikey=thewdb`);
    console.log(responseOne);
    console.log(responseTwo);
}

getMovieData();

// The responseOne request needs to be resolved before the second one..
// this can really slow down our code!


// We can make the requests first in parallel, then resolve promises
async function getMovieData(movieName) {
    var titanicPromise = $.getJSON(`https://omdbapi.com?t=titanic&apikey=thewdb`);
    var shrekPromise = $.getJSON(`https://omdbapi.com?t=shrek&apikey=thewdb`);

    var titaniData = await titanicPromise;
    var shrekData = await shrekPromise;

    console.log(titaniData);
    console.log(shrekData);
}

getMovieData();








// Await with Promise.all
// We can use Promise.all to await multiple resolved promises
async function getMovieData(first, second) {
    var moviesList = await Promise.all([
        $.getJSON(`https://omdbapi.com?t=${first}&apikey=thewdb`),
        $.getJSON(`https://omdbapi.com?t=${second}&apikey=thewdb`)
    ]);
    console.log(moviesList[0].Year);
    console.log(moviesList[1].Year);
}

getMovieData('shrek', 'blade');

// 2001
// 1998