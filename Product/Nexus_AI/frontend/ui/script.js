document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const output = document.querySelector("#output");

  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    const input = document.querySelector("input").value;

    try {
      const response = await fetch("/api/content-generator/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: input }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      output.textContent = result.content;
    } catch (error) {
      output.textContent = `Error: ${error.message}`;
    }
  });

  const navToggle = document.querySelector(".nav-toggle");
  const navItems = document.querySelector(".nav-items");

  if (navToggle) {
    navToggle.addEventListener("click", () => {
      navItems.classList.toggle("active");
    });
  }
});
