/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let h =s.trim()
    let a =h.split(" ")
    let n =a[a.length-1].length
   return n
};