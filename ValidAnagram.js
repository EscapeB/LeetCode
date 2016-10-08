/**
 * Created by Chasel on 2016/10/2.
 */
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    //用26长度的数组存储两个字符串各个字符出现的次数，如果两个字符串的各个字符出现次数一致，则说明两个字符串是可以通过打乱顺序来得到
    var bit = new Array(26);
    var isSame = true;
    //判断字符串的长度是否一致
    if (s.length !== t.length) {
        return false;
    }
    //字符统计数组初始化
    for (var i = 0; i < 26; i++) {
        bit[i] = 0;
    }
    //统计第一个字符串的字符次数
    for (i = 0; i < s.length; i++) {
        bit[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    }
    //消去第二个字符串的字符次数
    for (i = 0; i < t.length; i++) {
        bit[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;

    }
    //判断字符统计数组是否为空。为空说明两个字符串可以各个字符数相同。
    for (i = 0; i < 26; i++) {
        if (bit[i] != 0) {
            isSame = false;
            break;
        }
    }
    //返回结果
    if (isSame) {
        return true;
    }
    else {
        return false;
    }

};
//测试
var s = "anagram", t = "nagaram";
console.log(isAnagram(s, t));