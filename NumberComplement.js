/**
 * Created by Chasel on 2017/1/15.
 */
/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    var i=1;
    while (i<num)
    {
        i=i<<1;
    }
    return i-1-num;
    
};
console.log(findComplement(5));