/**
 * Created by Chasel on 2016/10/2.
 */
var sloveNQueens = function (n) {
    //用一个N维数组存储皇后位置。数组下表表示行，该位置的数据表示列，这样就不会存在行冲突的问题。
    var queenPos = new Array(n);
    //创建一个存储所有解的数组。
    var allSolution = [];
    //初始化皇后位置的数组
    for (var i = 0; i < n; i++) {
        queenPos[i] = -9999;
    }
    //判断函数，判断新位置与已有皇后是否冲突。
    var judge = function (p, q) {
        for (var i = 0; i < n; i++) {
            //判断q列是否与某一行的列冲突||判断斜向是否冲突，如果两个位置在斜方向在一条直线，那么行号之差等于列号之差。
            if (queenPos[i] === q || Math.abs(i - p) === Math.abs(queenPos[i] - q)) {
                return false;
            }
        }
        return true;
    }
    //将一个解加入到解集之中。
    var addSolution = function () {
        var i, j;
        var row = "";
        var solution = [];
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (queenPos[i] === j) {
                    row += "Q";
                }
                else {
                    row += "*";
                }
            }
            solution.push(row);
            row = "";
        }
        allSolution.push(solution);
    }
    var i = 0;
    var j = 0;
    //通过回溯法进行探测
    //首先对行进行探测
    while (i<n){
        //逐列探测
        while(j<n){
            //如果当前位置可以放置皇后，将queenPos数组该位置数据设为列，跳出列探测，在末尾i++，j归零
            if (judge(i,j)){
                queenPos[i]=j;
                j=0;
                break;
            }
            //如果当前位置不能放置皇后，j++，对下一列进行探测。
            else {
                j++;
            }
        }
        //如果列探测完，该queenPos该行位置上的数据仍未初始值
        if (queenPos[i]===-9999){
            //若i为0，说明回溯到头，没有其他解了。就结束
            if (i===0){
                break;
            }
            //若为其他值，返回上一行继续探测，从上一行记录列位置的下一列进行探测。
            else {
                i--;
                j=queenPos[i]+1;
                queenPos[i]=-9999;
                continue;
            }
        }
        //如果i为n-1，说明已经探测完最后一行且找到了解，记录解并从该记录解的下一列继续探测。将queenPos该位置设为初始值
        if(i===n-1){
            addSolution();
            j=queenPos[i]+1;
            queenPos[i]=-9999;
            continue;
        }
        i++;
    }
    function outputQueens(result) {
        console.log('total solves '+result.length);
        result.map(function (currentValue, index, array) {
           for (var i=0;i<currentValue.length;i++)
           {
               console.log(currentValue[i]+'\n');
           }
           console.log('-----------------------');
        });
    }
    outputQueens(allSolution);
};
sloveNQueens(4);