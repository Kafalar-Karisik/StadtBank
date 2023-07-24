var refreshIcon = document.getElementById("refresh");

refreshIcon.addEventListener("click", function () {
  refreshIcon.classList.add("rotate-animation");

  // Yenileme butonuna tıklandığında yapılacak işlemler
  // Örnek olarak sayfayı yenilemek için:
  location.reload();
});


function customerDet(nr) {
    window.location.href = window.location.origin + "/main/customers/" + nr
}