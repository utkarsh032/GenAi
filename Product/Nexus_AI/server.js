const express = require("express");
const { GoogleGenerativeAI } = require("@google/generative-ai");
require("dotenv").config();

const app = express();
const port = 3000;

// Initialize the Google Generative AI client with the API key from environment variables
const genAI = new GoogleGenerativeAI(process.env.API_KEY);

// Middleware to parse JSON request bodies
app.use(express.json());

// Serve static files from the "frontend" directory
app.use(express.static("frontend"));
// app.use(express.static(path.join(__dirname, 'frontend')));

// Endpoint for generating content
app.post("/generate-content", async (req, res) => {
  try {
    const model = await genAI.getGenerativeModel({ model: "gemini-pro" });
    const prompt = req.body.prompt;

    if (!prompt) {
      return res.status(400).json({ error: "Prompt is required" });
    }

    const result = await model.generateContent(prompt);
    const response = await result.response.text();
    res.json({ result: response });
  } catch (error) {
    console.error("Error generating content:", error);
    res
      .status(500)
      .json({ error: "An error occurred while generating content." });
  }
});

// Endpoint for generating images
app.post("/generate-image", async (req, res) => {
  try {
    const prompt = req.body.prompt;

    if (!prompt) {
      return res.status(400).json({ error: "Prompt is required" });
    }

    // Replace with actual image generation logic
    const imageUrl = await generateImageFromPrompt(prompt);
    res.json({ imageUrl });
  } catch (error) {
    console.error("Error generating image:", error);
    res
      .status(500)
      .json({ error: "An error occurred while generating the image." });
  }
});

// Endpoint for generating fantasy content
app.post("/generate-fantasy", async (req, res) => {
  try {
    const model = await genAI.getGenerativeModel({ model: "gemini-pro" });
    const prompt = req.body.prompt;

    if (!prompt) {
      return res.status(400).json({ error: "Prompt is required" });
    }

    const result = await model.generateContent(prompt);
    const response = await result.response.text();
    res.json({ result: response });
  } catch (error) {
    console.error("Error generating fantasy content:", error);
    res
      .status(500)
      .json({ error: "An error occurred while generating fantasy content." });
  }
});

// Serve the content generator page
app.get("/content-generator", (req, res) => {
  res.sendFile(
    __dirname + "/frontend/content-generator/content-generator.html"
  );
});

// Serve the image generator page
app.get("/image-generator", (req, res) => {
  res.sendFile(__dirname + "/frontend/image-generator/image-generator.html");
});

// Serve the fantasy generator page
app.get("/fantasy", (req, res) => {
  res.sendFile(__dirname + "/frontend/fantasy/fantasy.html");
});

// Endpoint for generating jokes
app.post("/generate-joke", async (req, res) => {
  try {
    const model = await genAI.getGenerativeModel({ model: "gemini-pro" });
    const prompt = req.body.prompt;

    if (!prompt) {
      return res.status(400).json({ error: "Prompt is required" });
    }

    const result = await model.generateContent(prompt);
    const response = await result.response.text();
    res.json({ result: response });
  } catch (error) {
    console.error("Error generating joke:", error);
    res
      .status(500)
      .json({ error: "An error occurred while generating the joke." });
  }
});

// Endpoint for generating Shayari
app.post("/generate-shayari", async (req, res) => {
  try {
    const model = await genAI.getGenerativeModel({ model: "gemini-pro" });
    const prompt = req.body.prompt;

    if (!prompt) {
      return res.status(400).json({ error: "Prompt is required" });
    }

    const result = await model.generateContent(prompt);
    const response = await result.response.text();
    res.json({ result: response });
  } catch (error) {
    console.error("Error generating Shayari:", error);
    res
      .status(500)
      .json({ error: "An error occurred while generating the Shayari." });
  }
});

app.get("/", (req, res) => {
  res.redirect("/ui/index.html");
});

// Placeholder function for generating image URL (replace with actual logic)
async function generateImageFromPrompt(prompt) {
  // Integrate with your image generation API or model
  return `https://via.placeholder.com/800x600.png?text=${encodeURIComponent(
    prompt
  )}`;
}

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
