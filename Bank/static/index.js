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
  { text: "Actions", href: "../actions" },
  { text: "Pay", href: "../pay" }
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

  let currentSortKey = null;
  let sortAscending = true;

  const sortTable = (key) => {
    currentSortKey = key;
    sortAscending = !sortAscending;

    const rows = Array.from(tbody.rows);
    const sortedRows = rows.sort((a, b) => {
      const cellA = a.cells[getKeyIndex(key)].innerText;
      const cellB = b.cells[getKeyIndex(key)].innerText;

      if (sortAscending) {
        return cellA.localeCompare(cellB);
      } else {
        return cellB.localeCompare(cellA);
      }
    });

    while (tbody.firstChild) {
      tbody.removeChild(tbody.firstChild);
    }

    sortedRows.forEach((row) => {
      tbody.appendChild(row);
    });
  };

  const getKeyIndex = (key) => {
    switch (key.toLowerCase()) {
      case "customer number":
        return 0;
      case "name":
        return 1;
      case "date action":
        return 2;
      case "action type":
        return 3;
      case "amount related":
        return 4;
      case "saldo":
        return 5;
      default:
        throw new Error(`Invalid key: ${key}`);
    }
  };

  Array.from(thead.rows[0].cells).forEach((cell) => {
    cell.addEventListener("click", () => {
      sortTable(cell.innerText);
    });
  });

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