// 버튼 이벤트
const backBtn = document.querySelector("#back-btn");
const homeBtn = document.querySelector("#home-btn");
const modifyBtn = document.querySelector("#modify-btn");
const logoutBtn = document.querySelector("#logout-btn");

function goPrevPage() {
  //뒤로가기
  window.history.back();
}

function goHome() {
  // 세계지도 페이지로 이동
  window.location.href = "world.html";
}

function modifyMyInfo() {
  //비밀번호 확인 페이지로 이동
  window.location.href = "check.html";
}

function logOut() {
  if (confirm("로그아웃 하시겠습니까?")) {
    sessionStorage.clear();
    window.location.href = "main.html";
  }
}

backBtn.addEventListener("click", goPrevPage);
homeBtn.addEventListener("click", goHome);
modifyBtn.addEventListener("click", modifyMyInfo);
logoutBtn.addEventListener("click", logOut);

// 유저 정보 받아오기
const userName = document.getElementById("username");
const userPic = document.querySelector("#pic-container > img");
const citylist = document.getElementById("city-list-div");

function getUser() {
  userName.innerText = "";
  userPic.src = "#";
}

getUser();

//내가 평가한 도시
