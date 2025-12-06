/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    data  =  nums.map((item)=>item * item)
   return  data.sort((a,b)=>a-b)
};