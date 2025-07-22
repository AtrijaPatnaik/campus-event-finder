// Get the search input and event elements
const searchInput = document.getElementById("searchInput");
const eventElements = document.querySelectorAll(".event");

searchInput.addEventListener("input", function () {
  const query = this.value.toLowerCase();

  eventElements.forEach(event => {
    const title = event.querySelector("h2").textContent.toLowerCase();
    const location = event.querySelectorAll("p")[1].textContent.toLowerCase();

    // Show the event if title or location includes the search term
    if (title.includes(query) || location.includes(query)) {
      event.style.display = "block";
    } else {
      event.style.display = "none";
    }
  });
});
