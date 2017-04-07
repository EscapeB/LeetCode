/**
 * Created by Chasel on 2017/3/13.
 */
/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    var max=Number.MAX_VALUE;
    var count=0;
    for (var i=0;i<s.length;i++){
        var index1=s.indexOf(Math.min.apply(Math,s));
        for (var j=0;j<g.length;j++) {
            var index2 = g.indexOf(Math.min.apply(Math, g));
            if (s[index1] >= g[index2]) {
                count++;
                g[index2] = max;
                s[index1] = max;
                break;
            }
        }
        if (count>=g.length){
            break;
        }
        s[index1]=max;
    }
    return count;
};
console.log(findContentChildren([1,2], [1,2,3]));