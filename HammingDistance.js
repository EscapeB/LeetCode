/**
 * Created by Chasel on 2017/1/15.
 */
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function (x, y) {
    var bitNumber = x ^ y;//将ｘ，ｙ中每位上不同的全都整合到一个数上，计算这个数有多少个１就是x，y中不同的位数
    var counter = 0;
    for (var i = 0; i < 32; i++) {//题中给出已知条件x,y都在32位以下
        if (bitNumber % 2 == 1) {//计算bitNumber的位数中1的个数
            counter++;
        }
        bitNumber = Math.floor(bitNumber / 2);
    }
    return counter;

};
console.log(hammingDistance(1,4));