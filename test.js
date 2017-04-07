var s=function (s) {
    var nums=[];
    var operator=[];
    for (var i=0;i<s.length;i++){
        if(!isNaN(parseInt(s.charAt(i)))){
            nums.push(parseInt(s.charAt(i)));
        }
        else
        {
            operator.push(s.charAt(i));

        }
    }
    while(nums.length!==1){
        var op=operator.pop();
        var opNext=operator.pop();
        if((op==="+"||op==="-")&&opNext==="*"){
            var num3=nums.pop();
            var num2=nums.pop();
            var num1=nums.pop();
            var newnum=num1*num2;
            nums.push(newnum);
            nums.push(num3);
            operator.push(op);
        }
        else{
            operator.push(opNext);
            var num2=nums.pop();
            var num1=nums.pop();
            var newnum;
            switch(op){
                case "*":newnum=num1*num2;break;
                case "+":newnum=num1+num2;break;
                case "-":newnum=num1-num2;break;
            }
            nums.push(newnum);
        }
    }
    var result=nums.pop();
    console.log(result);
}
s("1-2*3");