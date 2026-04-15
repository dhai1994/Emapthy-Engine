from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from pydub import AudioSegment
import asyncio
import edge_tts
import os
import uuid

app = Flask(__name__)

# ── Load emotion model once at startup ──────────────────────────────────────
print("Loading emotion model... (first run downloads ~250MB, be patient)")
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)
print("✅ Model loaded!")

# ── Edge TTS Voices — Male & Female per emotion ──────────────────────────────
# These are Microsoft Neural voices — HIGH QUALITY, FREE, no API key needed
VOICES = {
    "female": {
        "joy":      "en-US-AriaNeural",       # warm, expressive
        "anger":    "en-US-JaneNeural",        # assertive
        "sadness":  "en-US-SaraNeural",        # soft, gentle
        "fear":     "en-US-NancyNeural",       # nervous tone
        "surprise": "en-US-AriaNeural",        # expressive
        "disgust":  "en-US-JaneNeural",        # flat/measured
        "neutral":  "en-US-JennyNeural",       # professional
    },
    "male": {
        "joy":      "en-US-GuyNeural",         # upbeat
        "anger":    "en-US-TonyNeural",        # sharp, direct
        "sadness":  "en-US-EricNeural",        # deep, heavy
        "fear":     "en-US-RogerNeural",       # quiet, tense
        "surprise": "en-US-GuyNeural",         # expressive
        "disgust":  "en-US-TonyNeural",        # flat/measured
        "neutral":  "en-US-ChristopherNeural", # calm, clear
    }
}

# ── Emotion voice parameter mapping (rate, pitch, volume for edge-tts) ───────
EMOTION_CONFIG = {
    "joy":      {"rate": "+20%", "pitch": "+8Hz",  "volume": "+20%", "emoji": "😄", "color": "#FFD700"},
    "anger":    {"rate": "+15%", "pitch": "-4Hz",  "volume": "+30%", "emoji": "😠", "color": "#FF4444"},
    "sadness":  {"rate": "-25%", "pitch": "-6Hz",  "volume": "-15%", "emoji": "😢", "color": "#4A90D9"},
    "fear":     {"rate": "+10%", "pitch": "+4Hz",  "volume": "-10%", "emoji": "😨", "color": "#9B59B6"},
    "surprise": {"rate": "+25%", "pitch": "+10Hz", "volume": "+20%", "emoji": "😲", "color": "#FF8C00"},
    "disgust":  {"rate": "-10%", "pitch": "-3Hz",  "volume": "+0%",  "emoji": "🤢", "color": "#27AE60"},
    "neutral":  {"rate": "+0%",  "pitch": "+0Hz",  "volume": "+0%",  "emoji": "😐", "color": "#95A5A6"},
}

def detect_emotion(text):
    """Returns (emotion_label, confidence_score)"""
    result = emotion_classifier(text)[0][0]
    return result["label"], round(result["score"] * 100, 1)

def scale_rate(base_rate, intensity):
    """Scale the rate percentage based on confidence (intensity)"""
    if base_rate == "+0%":
        return "+0%"
    sign = "+" if "+" in base_rate else "-"
    num = float(base_rate.replace("+","").replace("-","").replace("%",""))
    scaled = num * (0.5 + intensity / 200)
    return f"{sign}{scaled:.0f}%"

async def generate_edge_tts(text, voice_name, rate, pitch, volume, output_path):
    """Async function to call edge-tts"""
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice_name,
        rate=rate,
        pitch=pitch,
        volume=volume
    )
    await communicate.save(output_path)

def generate_audio(text, emotion, confidence, gender):
    """Generate emotion-modulated audio using edge-tts, return filename"""
    config = EMOTION_CONFIG.get(emotion, EMOTION_CONFIG["neutral"])
    voice_name = VOICES.get(gender, VOICES["female"])[emotion]

    # Scale rate based on confidence
    scaled_rate = scale_rate(config["rate"], confidence)

    os.makedirs("static/audio", exist_ok=True)
    filename = f"output_{uuid.uuid4().hex[:8]}.mp3"
    filepath = f"static/audio/{filename}"

    # Run async edge-tts
    asyncio.run(generate_edge_tts(
        text=text,
        voice_name=voice_name,
        rate=scaled_rate,
        pitch=config["pitch"],
        volume=config["volume"],
        output_path=filepath
    ))

    return filename, voice_name

# ── Routes ───────────────────────────────────────────────────────────────────
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form.get("text", "").strip()
    gender = request.form.get("gender", "female").strip().lower()

    if not text:
        return jsonify({"error": "Please enter some text."}), 400
    if len(text) > 500:
        return jsonify({"error": "Text too long. Max 500 characters."}), 400
    if gender not in ["male", "female"]:
        gender = "female"

    emotion, confidence = detect_emotion(text)
    config = EMOTION_CONFIG[emotion]
    audio_file, voice_name = generate_audio(text, emotion, confidence, gender)

    return render_template(
        "result.html",
        text=text,
        emotion=emotion.upper(),
        confidence=confidence,
        emoji=config["emoji"],
        color=config["color"],
        audio_file=audio_file,
        gender=gender.capitalize(),
        voice_name=voice_name,
        rate=config["rate"],
        pitch=config["pitch"],
    )

if __name__ == "__main__":
    app.run(debug=True)
