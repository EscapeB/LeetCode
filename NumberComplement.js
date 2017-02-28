/**
 * Created by Chasel on 2017/1/15.
 */
/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    var i=1;
    /*if(num==0){return 1;}
    else if(num==1){return 0;}
    else if(num==Math.max()){return 0;}*/
    while (i<=num)
    {

        i=i<<1;
    }
    return ~num&(i-1);
    
};
console.log(findComplement(2147483647));