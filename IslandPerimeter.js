/**
 * Created by Chasel on 2017/3/1.
 */
/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function (grid) {
    var total = 0;
    var sub = 0;
    for (var i = 0; i < grid.length; i++) {
        for (var j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === 1) {
                total++;
                if (i > 0 && grid[i - 1][j] === 1) {
                    sub++;
                }
                if (j > 0 && grid[i][j - 1] === 1) {
                    sub++;
                }
            }
        }
    }
    return total * 4 - sub * 2;
};
console.log(islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]));
