/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    // let ans2 = nums.filter((v,i)=> v === target  )
    if(nums.includes(target)){
        let ans1 = nums.map((v,i)=> v === target ? i : undefined).filter(v=> v !== undefined)
    return ans1[0]
    }else{
        return -1
    }
    
};