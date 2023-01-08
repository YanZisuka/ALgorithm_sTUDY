const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './_input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

di = [-1, 1, 0, 0];
dj = [0, 0, -1, 1];

function bfs([si, sj]) {
  const q = [];
  q.push([si, sj]);
  visited[si][sj] = 1;
  let area = 1;

  while (q.length) {
    const [ci, cj] = q.shift();
    for (let k = 0; k < di.length; k++) {
      [ni, nj] = [ci + di[k], cj + dj[k]];

      if (
        !(ni < 0 || nj < 0 || ni >= n || nj >= m) &&
        !visited[ni][nj] &&
        board[ni][nj] === 1
      ) {
        visited[ni][nj] = 1;
        q.push([ni, nj]);
        area++;
      }
    }
  }
  return area;
}

const [n, m] = input[0].split(' ').map((el) => +el);
const board = Array.from(input.slice(1), (arr) =>
  arr.split(' ').map((el) => +el)
);
const visited = Array.from(Array(n), () => Array(m).fill(0));
let [num, area] = [0, 0];

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 1 && !visited[i][j]) {
      const tmp = bfs([i, j]);
      num++;
      area = area >= tmp ? area : tmp;
    }
  }
}

console.log(num);
console.log(area);
