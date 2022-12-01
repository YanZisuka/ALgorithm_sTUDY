let fs = require("fs");
let filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let [f, s, g, u, d] = input[0].split(" ").map(Number);
let visited = new Array(1000001).fill(0);

function bfs(st) {
  let q = [];
  q.push(st);
  visited[st] = 1;
  let cnt = 0;

  while (q.length) {
    let r = q.length;
    for (let i = 0; i < r; i++) {
      let ci = q.shift();
      if (ci === g) return cnt;

      [+u, -d].forEach((delta) => {
        let ni = ci + delta;
        if (ni >= 1 && ni <= f && !visited[ni]) {
          visited[ni] = 1;
          q.push(ni);
        }
      });
    }
    cnt += 1;
  }
  return undefined;
}

let answer = bfs(s);
if (answer === undefined) console.log("use the stairs");
else console.log(answer);
