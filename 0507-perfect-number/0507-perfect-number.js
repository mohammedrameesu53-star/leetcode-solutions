/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
    let a = 0 
    for(i =  1 ; i<num ; i++){
        if (num%i==0){
            a += i
        }
    }
    return a==num?true:false
};