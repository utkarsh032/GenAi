document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("fantasy-form");
  const outputDiv = document.getElementById("output");
  const jokeBtn = document.getElementById("joke-btn");
  const shayariBtn = document.getElementById("shayari-btn");

  // Track selected type
  let selectedType = "";

  // Handle button clicks to set the selected type and placeholder
  jokeBtn.addEventListener("click", () => {
    selectedType = "joke";
    updatePlaceholder("Enter your joke prompt here");
    console.log("Selected type: joke");
  });

  shayariBtn.addEventListener("click", () => {
    selectedType = "shayari";
    updatePlaceholder("Enter your Shayari prompt here");
    console.log("Selected type: shayari");
  });

  // Function to update the placeholder text
  function updatePlaceholder(text) {
    const textarea = form.querySelector("textarea");
    if (textarea) {
      textarea.placeholder = text;
    }
  }

  // Handle form submission
  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const prompt = document.getElementById("prompt").value.trim();
    if (!prompt) {
      alert("Prompt cannot be empty.");
      return;
    }

    if (!selectedType) {
      alert("Please select either 'Generate Joke' or 'Generate Shayari'.");
      return;
    }

    const API_URL = `/generate-${selectedType}`; // Dynamic API URL based on selected type

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      outputDiv.textContent = data.result || "No result returned.";
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to generate content. Please try again.");
    }
  });
});
