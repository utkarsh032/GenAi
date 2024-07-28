document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("image-generator-form");
  const outputImage = document.getElementById("image");

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const prompt = document.getElementById("input").value;

    try {
      const response = await fetch("/generate-image", {
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
      const imageUrl = data.imageUrl; // Adjust based on the actual response structure

      outputImage.src = imageUrl;
      outputImage.alt = "Generated Image";
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to generate image. Please try again.");
    }
  });
});
