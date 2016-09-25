/**
 * Created by Chasel on 2016/9/25.
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var maxDepth = function (root) {
    var max = 0;
    if (arguments[0] == null) {
        return 0;
    }
    var left=arguments.callee(root.left)+1;
    var right=arguments.callee(root.right)+1;
    max=(left>right)?left:right;
    return max;
};
var root = new TreeNode(0);
root.left = new TreeNode(1);
root.right = new TreeNode(2);
root.left.left = new TreeNode(3);
root.left.right = new TreeNode(4);
root.right.left = new TreeNode(5);
root.left.left.left = new TreeNode(6);
console.log(maxDepth(root));