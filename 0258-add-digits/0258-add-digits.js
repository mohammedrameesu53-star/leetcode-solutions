/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
   
for(;;){
let a =String(num)
if(a.length === 1){
    return Number(a) 
    break;
}
let b = 0;
for(let i =0; i<a.length; i++){
    b += Number(a[i])
}
num = b

}
   
};