/**
 * Created by Chasel on 2017/3/11.
 */
/**
 * @param {number} num
 * @return {string[]}
 */
var readBinaryWatch = function (num) {
    var out = [];
    var countBit = function (n) {
        var bit = 0;
        while (n > 0) {
            bit++;
            n &= n - 1;
        }
        return bit;
    }
    for (var h = 0; h < 12; h++) {
        for (var min = 0; min < 60; min++) {
            if ((countBit(h) + countBit(min)) === num) {
                var temp = "";
                if (min < 10) {
                    temp += h.toString() + ":0" + min.toString();
                }
                else {
                    temp += h.toString() + ":" + min.toString();
                }
                out.push(temp);
            }
        }
    }
return out;
};
console.log(readBinaryWatch(1));