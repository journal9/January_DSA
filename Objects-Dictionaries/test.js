
a={'abc':34,"acb":24,"fgh":98}
// let sort_k = Object.fromEntries(Object.entries(a).sort().reduce(
//     ([a,],[b,])=>a-b
// ))
// console.log(sort_k)

let k=Object.fromEntries(Object.entries(a).sort(
    ([a,],[b,])=>a-b
))
console.log(k)