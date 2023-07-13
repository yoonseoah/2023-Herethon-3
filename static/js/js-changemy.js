const backBtn = document.querySelector("#back-btn");
const homeBtn = document.querySelector("#home-btn");
const saveBtn = document.querySelector("#save-btn");
function goPrevPage() {
  //뒤로가기
  window.history.back();
}

function goHome() {
  // 세계지도 페이지로 이동
  window.location.href = "world.html";
}

function sendInfo() {
  //form에 입력된 정보 DB로 전송
}

function saveChangedInfo() {
  if (window.confirm("개인정보를 수정하시겠습니까?")) {
    alert("개인정보 수정 완료");
    //수정된 정보 데이터 전송 function
    window.location.href = "mypage.html";
  } else {
    console.log("사용자답변: 취소 - 변화없음");
  }
}

backBtn.addEventListener("click", goPrevPage);
homeBtn.addEventListener("click", goHome);
saveBtn.addEventListener("click", saveChangedInfo);

//프로필 사진 수정 div에 이벤트 추가
window.onload = function () {
  var editPicDiv = document.getElementById("edit-pic-container");
  editPicDiv.onclick = editProfile;
};

function editProfile() {
  console.log("editProfile");
  //프로필 사진 수정 함수
}
