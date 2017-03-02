/**
 * Created by Chasel on 2017/3/2.
 */
/**
 * @param {number} area
 * @return {number[]}
 1. The area of the rectangular web page you designed must equal to the given target area.

 2. The width W should not be larger than the length L, which means L >= W.

 3. The difference between length L and width W should be as small as possible.
 */
var constructRectangle = function(area) {
    var difference=Number.MAX_VALUE;
    var width=0,long=0;
    for (var i=1;i<=Math.sqrt(area);i++){
        if(area%i===0){
            if(area/i-i<difference){
                width=i;
                long=area/i;
                difference=area/i-i;
            }
        }
    }
    return [long,width];
};
console.log(constructRectangle(48));