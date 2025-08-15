const API_URL ="https://api.render.com/deploy/srv-d2cp7ier433s73au3gdg?key=V6iyR-QdQjY";

document.getElementById("analyzeBtn").addEventListener("click", analyzeSentiment);

async function analyzeSentiment() {
  const text = document.getElementById("inputText").value;
  if (!text) {
    alert("Please enter some text.");
    return;
  }

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    if (!res.ok) {
      throw new Error(`Server error: ${res.status}`);
    }

    const data = await res.json();
    document.getElementById("result").innerHTML =
      `Prediction: ${data.prediction} <br> Probability: ${data.probability.toFixed(2)}`;

  } catch (error) {
    alert("Failed to connect to backend: " + error.message);
  }
}


