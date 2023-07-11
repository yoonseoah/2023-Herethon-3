const backBtn = document.querySelector("#back-btn");
function goPrevPage() {
  //뒤로가기
  window.history.back();
}
backBtn.addEventListener("click", goPrevPage);

const startBtn = document.querySelector("#start-btn");
function goWorld() {
  window.location.href = "world.html";
}
startBtn.addEventListener("click", goWorld);

//사용자 데이터 받아오기 필요
const profilePic = document.getElementById("profile-pic");
const nickname = document.getElementById("username");

function getUserInfo() {
  profilePic.src = "";
  nickname.innerText = "";
}
