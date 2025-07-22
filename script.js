// Event filtering
const searchInput = document.getElementById("searchInput");
const eventElements = document.querySelectorAll(".event");

searchInput.addEventListener("input", function () {
  const query = this.value.toLowerCase();

  document.querySelectorAll(".event").forEach(event => {
    const title = event.querySelector("h2").textContent.toLowerCase();
    const location = event.querySelectorAll("p")[1].textContent.toLowerCase();

    if (title.includes(query) || location.includes(query)) {
      event.style.display = "block";
    } else {
      event.style.display = "none";
    }
  });
});

// Adding new events
document.getElementById("addEventBtn").addEventListener("click", function () {
  const title = document.getElementById("eventTitle").value;
  const date = document.getElementById("eventDate").value;
  const location = document.getElementById("eventLocation").value;

  if (title && date && location) {
    const eventSection = document.getElementById("events");

    const newEvent = document.createElement("div");
    newEvent.className = "event";
    newEvent.innerHTML = `
      <h2>${title}</h2>
      <p>Date: ${new Date(date).toLocaleDateString()}</p>
      <p>Location: ${location}</p>
    `;

    eventSection.appendChild(newEvent);

    // Clear form
    document.getElementById("eventTitle").value = "";
    document.getElementById("eventDate").value = "";
    document.getElementById("eventLocation").value = "";
  } else {
    alert("Please fill in all fields.");
  }
});
