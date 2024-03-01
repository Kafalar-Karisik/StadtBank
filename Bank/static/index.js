//<tr onclick="customerDet({{customer.nr}})">

var refreshIcon = document.getElementById("refresh");
refreshIcon.addEventListener("click", function () {
    refreshIcon.classList.add("rotate-animation");

    location.reload();
});


function customerDet(nr) {
    window.location.href = window.location.origin + "/customers/" + nr
}

