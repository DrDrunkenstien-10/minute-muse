# MinuteMuse

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**MinuteMuse** is an AI-powered tool for automating the generation of meeting minutes and action items from meeting transcriptions. By leveraging advanced audio processing and language models, MinuteMuse simplifies post-meeting workflows and improves productivity.

## ✨ Features

- 🎥 Accepts **video**, **audio**, or **text transcripts** as input
- 🔊 Converts video to audio using `ffmpeg`
- 🤖 Transcribes audio to text using **OpenAI Whisper**
- 🧠 Summarizes transcripts into meeting minutes using **Mistral AI**
- 📄 Outputs clean, structured **Markdown** minutes
- 🖥️ Simple Flask UI to upload and view results
- 💾 Option to **download** the generated minutes
- ⚙️ Local installation, fully open-source under MIT License
---

## 🧩 Upcoming Features
The project is actively being improved! Planned enhancements include:

-  Project management integration – Automatically create tasks or boards in tools like Jira, Trello, or Wekan

- AI chatbot interface – Ask questions like “What decisions were made?”, “Who was assigned what?”, or “What did Mike say about timelines?”

💬 Have a feature in mind? Open an issue or suggest it in the Discussions tab!

## 🛠️ Tech Stack

- Python 3.8+
- Flask (for the web interface)
- ffmpeg (video to audio conversion)
- Whisper (speech-to-text)
- Mistral API (for summary generation)

---

## 🚀 Getting Started (Local Setup)

### 📦 Requirements

- Python 3.8 or newer
- `ffmpeg` installed and in your system PATH
- API key for Mistral AI (set as environment variable)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/minute_muse.git
   cd minute_muse
   ```

2. Create a virtual environment and activate it:
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

   ```
4. Set up the environment variables:

   Create a .env file in the project root.
   Add the following variables:
   ```bash
   MISTRAL_API_KEY=<MISTRAL_API_KEY>
   ```

5. Install FFmpeg:

- macOS:

   ```bash
   brew install ffmpeg
   ```

- Ubuntu/Debian:

   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

- Windows:

   Download from: https://ffmpeg.org/download.html

   
   Add ffmpeg/bin to your system PATH  


6. Run the Flask App

   ```bash
   python3 run_flask.py
   ```
Then, open your browser and go to: http://localhost:5000

## Sample Input Formats
- Video: .mp4, .mov, .avi
- Audio: .mp3, .wav, .m4a
- Text: Plain .txt transcripts

## Output
- Markdown-formatted minutes
- Option to view or download from the UI

## 🤝 Contributing
PRs, issues, and suggestions are welcome!
If you find this useful, consider giving a ⭐ on GitHub!

## 📜 License
This project is licensed under the Apache 2.0 License.
Feel free to use, modify, and distribute with attribution.

## 🙋‍♂️ Author
Atharva Jadhav
Built with ❤️ to save your time during boring meetings.
