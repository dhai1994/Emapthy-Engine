# 🎭 The Empathy Engine — Giving AI a Human Voice

## 🚀 Overview

The Empathy Engine is an AI-powered web application that detects human emotions from text and converts them into expressive speech.

Unlike traditional text-to-speech systems, this project enhances communication by incorporating **emotional intelligence + multi-voice AI speech synthesis**, creating a more human-like interaction.

---

## 💡 Core Idea

Instead of generating flat, robotic audio, this system:

* Understands the **emotion behind text**
* Maps emotions to voice characteristics
* Generates expressive speech using **neural voices**
* Creates a more **human-like AI interaction experience**

---

## 🧠 Features

### 🔍 Emotion Detection

Detects 7 emotions:

* Joy 😄
* Anger 😠
* Sadness 😢
* Fear 😨
* Surprise 😲
* Disgust 🤢
* Neutral 😐

---

### 🔊 Multi-Voice AI Speech (NEW 🔥)

* Supports **multiple natural voices**:

  * Female (US)
  * Male (US)
  * Female (UK)
  * Male (UK)
* Built using **Microsoft Edge Neural TTS (edge-tts)**
* Much more realistic than basic TTS systems

---

### 🎚️ Emotion-Based Voice Modulation

* Adjusts:

  * Speed
  * Tone (simulated)
* Enhances emotional delivery of speech

---

### 🎨 Dynamic User Interface

* Dark futuristic UI
* Emotion-based visual feedback
* Smooth animations + modern design

---

### 📊 Emotion Confidence Indicator

* Displays prediction confidence
* Improves transparency of AI decisions

---

### 📝 Recent History (Custom Feature)

* Stores **last 5 user inputs**
* Click to reuse previous inputs
* Stored using browser localStorage

---

### 🎧 Audio Visualization

* Real-time waveform animation synced with audio

---

## 🛠️ Technologies Used

* **Flask** — Backend web framework
* **HuggingFace Transformers** — Emotion detection model
* **Edge-TTS** — Neural text-to-speech (multi-voice support)
* **pydub + FFmpeg** — Audio processing
* **HTML, CSS, JavaScript** — Frontend UI

---

## ⚙️ How It Works

1. User enters text input
2. AI model detects emotion + confidence score
3. User selects voice
4. Text is converted into speech using neural TTS
5. Audio is played with waveform visualization
6. Result displayed with emotion insights

---

## 🧩 Project Structure

```id="h17sqk"
empathy-engine/
│── app.py
│── requirements.txt
│── static/
│   └── audio/
│── templates/
│   ├── index.html
│   └── result.html
```

---

# 🚀 ▶️ HOW TO RUN (VERY IMPORTANT)

## 1️⃣ Clone the Repository

```bash id="8xqltt"
git clone https://github.com/your-username/empathy-engine.git
cd empathy-engine
```

---

## 2️⃣ Install Python (Recommended)

👉 Use:

```id="o6sm0d"
Python 3.11
```

---

## 3️⃣ Install Dependencies

```bash id="yzkqoj"
py -3.11 -m pip install -r requirements.txt
```

---

## 4️⃣ Install FFmpeg (Required)

### Windows:

1. Download from: https://ffmpeg.org/download.html
2. Extract → copy `bin` folder path
3. Add to **Environment Variables (PATH)**

---

## 5️⃣ Run the Application

```bash id="s5m3yo"
py -3.11 app.py
```

---

## 6️⃣ Open in Browser

```id="m27r9c"
http://localhost:5000
```

---

# ⚠️ Common Issues & Fixes

### ❌ ModuleNotFoundError (edge-tts)

```bash id="q9b3nt"
py -3.11 -m pip install edge-tts
```

---

### ❌ FFmpeg not found

👉 Ensure FFmpeg `bin` folder is added to PATH

---

### ❌ Audio not playing

👉 Check:

```id="0t7x2c"
static/audio/output.mp3
```

---

# 🎯 Key Highlights

* Real-time emotion detection
* Multi-voice neural speech synthesis
* Modern AI-style UI
* Audio waveform visualization
* Persistent user interaction history

---

# 🎯 Future Improvements

* 🎤 Voice input (Speech-to-Text)
* 🌍 Multi-language support
* 🎛️ Advanced voice control (pitch, tone)
* 📊 Emotion analytics dashboard

---

# 👨‍💻 Author

Dhairya Rathore

---

# ⭐ Final Note

This project demonstrates how AI can move beyond logic and incorporate **emotional intelligence + human-like voice interaction**, making communication more natural and engaging.

> “An AI system that understands not just what you say, but how you feel.”
