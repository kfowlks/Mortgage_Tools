const tabs = document.querySelectorAll(".tabs li");
const tabContentBoxes = document.querySelectorAll("#tab-content > div");

// Bulma Tabs - These tabs function based on the content in the tabs are pre-rendered
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((items) => items.classList.remove("is-active"));
    tab.classList.add("is-active");

    const target = tab.dataset.target;
    console.log(target);
    tabContentBoxes.forEach((box) => {
      if (box.getAttribute("id") === target) {
        box.classList.remove("is-hidden");
      } else {
        box.classList.add("is-hidden");
      }
    });
  });
});
