const user = {
    name: "Talha",
    age: 26,
    marks: {
      math: 20,
      eng:30
    }
  };

//accessing elements of an object
console.log(user.marks.math)
console.log(user['marks']['math'])

//get list of key and values
let keys = Object.keys(user)
console.log(keys)
let values = Object.values(user)
console.log(values)
//give key values only for 1 level deep
let items = Object.entries(user)
console.log(items)

//adding a new key-value in object
Object.assign(user,{"street":24});
console.log(user)

//delete a key-value pair
delete user.street

//If a key is present in an object
console.log('name' in user)
console.log('math' in user.marks)
console.log(user.hasOwnProperty('name'))
console.log(user?.marks?.science!==undefined)

// Object.freeze(user)
// Object.seal(user)

//Copying an Object

//SHALLOW COPY
//deeper values will be referenced
let clone = {...user}
let clone2 = Object.assign({},user)
//DEEP COPY
//no values will be referenced
let clone3 = JSON.parse(JSON.stringify(user))
console.log(clone)

//------solution
// const _ = require('lodash');
// let good_cloned = _.cloneDeep(user)

// combining 2 objects
// const combineObj = Object.assign(user1, user1NewVal)

// Object.freeze(user)
// Object.seal(user)


let score = {'math':100,"science":90,"Geography":81}
//sorting objects
//sort by keys
const sk = Object.keys(score).sort().reduce(
    (obj,key)=>{
        obj[key] = score[key]
        return obj
    },{}
)
let sk2 = Object.fromEntries(
    Object.entries(score).sort(([a,],[b,])=>a-b)
)
console.log("sorting by keys")
console.log(sk)
console.log(sk2)

//sort by values
console.log("sorting by values")
const sv = Object.entries(score).sort((a,b) => a[1]-b[1])
console.log(sv)

let fv = Object.fromEntries(
    Object.entries(score).sort(([,a],[,b])=>a-b)
)
console.log(fv)
// object-->array-->sort array-->create object from array

//return key for a value
let val_key = Object.keys(score).find(key =>
    score[key] === 90);

console.log(val_key)