 let a=[2,4,6,8,4,3,9,10]

//length of the array
console.log(a.length)

//converts to string (values joined by ,)
console.log(a.toString())

//returns value at tyhe index
console.log(a.at(4))

//checks if value is present in the array
console.log(a.includes(10))

//for sorting numeric arrays in ascending order
a.sort(function (a,b){ return a-b})
console.log(a)

//for sorting numeric arrays in descending order
a.sort(function (a,b){ return b-a})
console.log(a)

//return the first value that matches
let borrow = a.find(function(value,index,array){
    return value % 3==0
})
console.log(borrow)

//a.findIndex()
//a.findLast()
//a.findLastIndex()

b=['aa','ac','bs','mn','et']
console.log(b)
let c = b.join('-')
console.log(c)

//used to add new items to an array
// The first parameter defines the position where new elements should be added (spliced in).
// The second parameter defines how many elements should be removed.
// The rest of the parameters define the new elements to be added.
let k = b.splice(1,2,"vyoy")
console.log(k)

//for removing items from an array
//.slice(start,end)
let m = b.slice(1,2)
console.log(m)

console.log(b)

let y = ['aa','sv','ba']
console.log(y)

console.log("sorting alphanumeric")
//asc order
console.log(y.sort())
//desc order
console.log(y.sort().reverse())

let d = y.sort()
console.log(d)
d.push('kkm')
console.log(d)
console.log(y)
//sort(), reverse() do not create copies of the array

//copy ann array
let t = [...b]
console.log(t)
//.slice()
//.map()
//.filter()
//numbersCopy = JSON.parse(JSON.stringify(nestedNumbers));
//numbersCopy = Array.from(numbers);

let u = [1,2,3,4,5,6,7,8,9,10]
//forEach
let sum =0
console.log("for each")
u.forEach(function (item){return sum+= item})
console.log(sum)

//map()
console.log("map")
let v = u.map(x=>x+10)
console.log(v)
console.log(u)

//filter
console.log("filter")
let w = u.filter(x=>x%4==0)
console.log(w) 

//reduce
let x = u.reduce((a,b,c)=>a+b+c)
console.log(x) 

console.log(1+2+3+4+5+6+7+8+9+10)

let z = u.reduce((num,index)=>num+index)
console.log(z) 