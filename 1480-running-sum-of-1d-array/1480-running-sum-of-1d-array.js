/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let a = []
    let n = 0
    for(i=0;i<nums.length;i++){
        n += nums[i]
        a.push(n)
    }
    return a
};