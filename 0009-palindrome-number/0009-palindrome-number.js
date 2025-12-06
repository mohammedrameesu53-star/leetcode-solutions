/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var a = String(x)
    let b = "";
    for(let i=a.length-1;i>=0;i--){
        
        b += a[i];
        
    }

    if( a == b){
        return true;
    }else{
        return false;
    }

};