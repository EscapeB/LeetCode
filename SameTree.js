/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    //判断是否到了树的叶子结点，如果同为叶子，返回true
    if (p == null && q == null) {
        return true;
    }
    //如果一个为空一个不为空，则说明不一致，返回false
    else if (p == null || q == null) {
        return false;
    }
    //判断当前结点的值是否相同，相同的话对其左右子树进行递归，并用&&进行结合。
    else if (p.val == q.val) {
        return arguments.callee(p.left, q.left) && arguments.callee(p.right, q.right);
    }
    else {
        return false;
    }
};

console.log(isSameTree([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]));