//<tr onclick="customerDet({{customer.nr}})">
/*
var refreshIcon = document.getElementById("refresh");
refreshIcon.addEventListener("click", function () {
    refreshIcon.classList.add("rotate-animation");

    location.reload();
});
*/

function customerDet(nr) {
  window.location.href = window.location.origin + "/customers/" + nr
}

// Define menu items as an array of objects for better organization
var menuItems = [
  { text: "Dashboard", href: "/" },
  { text: "Customers", href: "../customers" },
  //{ text: "Actions", href: "../actions" },
  { text: "Pay", href: "../pay" },
  { text: "Credit", href: "../creditManagment" }
];

// Create a function to dynamically generate the menu
var containerDiv = document.getElementById("menuList");

// Clear existing content inside the containerDiv
containerDiv.innerHTML = "";

// Create and append each <a> element
menuItems.forEach(function (item) {
  var menuItem = document.createElement("a");
  menuItem.href = item.href;
  menuItem.className = "pl-3 text-gray-200";
  menuItem.textContent = item.text;
  containerDiv.appendChild(menuItem);
});


const table = document.getElementById("customer-table");
if (table) {
  const thead = table.getElementsByTagName("thead")[0];
  const tbody = table.getElementsByTagName("tbody")[0];
  const searchInput = document.getElementById("customerSearchInput");

  if (searchInput) {
    searchInput.addEventListener("input", () => {
      const searchTerm = searchInput.value.toLowerCase();
      const rows = tbody.rows;

      for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].cells;
        const shouldShow = Array.from(cells).slice(0, 2).some((cell) =>
          cell.innerText.toLowerCase().includes(searchTerm),
        );

        if (shouldShow) {
          rows[i].style.display = "";
        } else {
          rows[i].style.display = "none";
        }
      }
    });
  }
}