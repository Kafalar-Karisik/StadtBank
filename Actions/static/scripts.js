var refreshIcon = document.getElementById("refresh");

refreshIcon.addEventListener("click", function () {
  refreshIcon.classList.add("rotate-animation");

  // Yenileme butonuna tıklandığında yapılacak işlemler
  // Örnek olarak sayfayı yenilemek için:
  location.reload();
});


function customerDetails(nr) {
    window.location.href = window.location.origin + "/customers/" + nr
}

function actionDetails(nr) {
  window.location.href = window.location.origin + "/actions/" + nr
}