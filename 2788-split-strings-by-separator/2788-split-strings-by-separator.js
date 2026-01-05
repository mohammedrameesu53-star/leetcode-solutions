/**
 * @param {string[]} words
 * @param {character} separator
 * @return {string[]}
 */
var splitWordsBySeparator = function(words, separator) {
    let a = []
    for(i=0;i<words.length;i++){
        a.push(words[i].split(separator))
    }
    let b = a.flat()
    let c= b.filter(v=> v !== "")
    return c
};