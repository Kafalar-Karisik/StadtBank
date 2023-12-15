var refreshIcon = document.getElementById("refresh");

if (refreshIcon) {
  refreshIcon.addEventListener("click", function () {
    refreshIcon.classList.add("rotate-animation");
    location.reload();
  });
}



function customerDetails(nr) {
    window.location.href = window.location.origin + "/customers/" + nr
}

function actionDetails(nr) {
  window.location.href = window.location.origin + "/actions/" + nr
}


document.addEventListener('DOMContentLoaded', function () {
  const tabs = document.querySelectorAll('.tabs li');
  const tabContents = document.querySelectorAll('.tab-content');

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
      // Remove is-active class from all tabs and is-hidden from all tab contents
      tabs.forEach((t) => t.classList.remove('is-active'));
      tabContents.forEach((tc) => tc.classList.add('is-hidden'));

      // Add is-active class to the clicked tab and display the corresponding content
      tab.classList.add('is-active');
      tabContents[index].classList.remove('is-hidden');
    });
  });
});


/*
const inputElements = document.querySelectorAll('.input');

function toggleInputStates() {
  inputElements.forEach(input => {
    input.classList.toggle('is-active');
    input.classList.toggle('is-loading');
  });
}
*/