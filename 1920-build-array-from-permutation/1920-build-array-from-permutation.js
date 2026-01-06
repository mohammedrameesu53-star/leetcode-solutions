/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function (nums) {
    let a = []
    for (i = 0; i < nums.length; i++) {
        a.push(nums[nums[i]])
    }
    return a
};