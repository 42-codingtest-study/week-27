//문제: 11729
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  arr = [
    [1, 2],
    [1, 3],
    [2, 3],
  ];
  const make_right = (arr) => {
    const answer = arr.map((e) => {
      if (e === 2) e = 3;
      else if (e === 3) e = 2;
    });
    return answer;
  };
  const answer = [[[1, 3]]];
  for (let i = 0; i < 20; i++) {
    const a = [];
    const b = [];
    answer[i].forEach((e) => {
      const aa = [];
      const bb = [];
      e.forEach((k) => {
        if (k === 2) aa.push(3);
        else if (k === 3) aa.push(2);
        else aa.push(k);
      });

      e.forEach((k) => {
        if (k === 1) bb.push(2);
        else if (k === 2) bb.push(1);
        else bb.push(k);
      });
      a.push(aa);
      b.push(bb);
    });
    const next = [...a, [1, 3], ...b];
    answer.push(next);
  }
  console.log(answer[+input[0] - 1].length);
  answer[+input[0] - 1].forEach((e) => {
    console.log(`${e[0]} ${e[1]}`);
  });
}
