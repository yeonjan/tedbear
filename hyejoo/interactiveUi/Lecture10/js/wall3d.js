(function () {
  // 벽들을 포함하고 있는 house를 이동시킬 예정이다

  const stageElem = document.querySelector(".stage");
  const houseElem = document.querySelector(".house");
  const barElem = document.querySelector(".progress-bar");
  const selectCharacterElem = document.querySelector(".select-character");
  const mousePos = { x: 0, y: 0 };
  let maxScrollValue;

  function resizeHandler() {
    //  전체 스클로 할 수 있는 범위
    maxScrollValue = document.body.offsetHeight - window.innerHeight;
  }

  //   스크롤 범위
  // 스크롤 끝 => 문서 전체 높이(body)에서 스크롤 바 높이만큼 빼야 함
  window.addEventListener("scroll", function () {
    //  스클로 얼마나했는지 비율
    const scrollPer = window.scrollY / maxScrollValue;
    const zMove = scrollPer * 980 - 490;
    houseElem.style.transform = "translateZ(" + zMove + "vw)";

    // progress bar
    barElem.style.width = scrollPer * 100 + "%";
  });

  window.addEventListener("mousemove", function (e) {
    mousePos.x = -1 + (e.clientX / window.innerWidth) * 2;
    mousePos.y = 1 - (e.clientY / window.innerHeight) * 2;
    stageElem.style.transform =
      "rotateX(" + mousePos.y * 5 + "deg) rotateY(" + mousePos.x * 5 + "deg)";
  });

  window.addEventListener("resize", resizeHandler);

  stageElem.addEventListener("click", function (e) {
    new Character({
      xPos: (e.clientX / window.innerWidth) * 100,
      speed: Math.random() * 0.5 + 0.2,
    });
  });

  selectCharacterElem.addEventListener("click", function (e) {
    const value = e.target.getAttribute("data-char");
    document.body.setAttribute("data-char", value);
  });

  resizeHandler();
})();
// 즉시 실행
