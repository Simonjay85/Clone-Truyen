const tests = [
  "## CHƯƠNG 1: Sáu Trăm",
  "## Chương 1: Sáu",
  "## CHƯơNG 1: Sáu"
];

const r1 = /^\s*(?:#{1,4}\s*)?(?:chương|chuong)\s+(\d+)\s*[:.;\-–—]?\s*(.*?)$/gmiu;

for (let t of tests) {
  r1.lastIndex = 0;
  console.log(t, r1.exec(t));
}
