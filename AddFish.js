/**
 * Created by Chasel on 2017/3/13.
 */
var addFish=function (minSize,maxSize,n,fishSize) {
    var result=[];
    var put=function (newFish,currentFish) {
        if ((newFish>=currentFish*2&&newFish<=currentFish*10)||(currentFish>=newFish*2&&currentFish<=newFish*10)){
            return false;
        }
        else {
            return true;
        }
    }
    for (var i=minSize;i<=maxSize;i++){
        var canput=true;
        for (var j=0;j<n;j++){
            if (!put(i,fishSize[j])){
                canput=false;
            }
        }
        if (canput){
            result.push(i);
        }
    }
    return result.length;
}
console.log(addFish(1,36,1,[3]));