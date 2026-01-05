/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function(words, x) {
    let ans = []
    for(i=0;i<words.length;i++){
        let bolean = words[i].includes(x)
        if(bolean){
            ans.push(i)
        }
    }

    return ans
};