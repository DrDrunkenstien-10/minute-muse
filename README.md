# MinuteMuse

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

**MinuteMuse** is an AI-powered tool for automating the generation of meeting minutes and action items from meeting transcriptions. By leveraging advanced audio processing and language models, MinuteMuse simplifies post-meeting workflows and improves productivity.

## Features

- **Audio Extraction**: Convert video files into high-quality audio.
- **Audio Chunking**: Split large audio files into manageable chunks for processing.
- **Speech-to-Text**: Use OpenAI's Whisper to transcribe audio files.
- **AI-Powered Summarization**: Generate concise meeting summaries and action items using the Mistral AI model.
- **Easy-to-Read Minutes**: Outputs meeting minutes in Markdown format for easy sharing and collaboration.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

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

- Create a .env file in the project root.
- Add the following variables

5. Install FFmpeg for audio processing:

- FFmpeg Download and Installation Guide

## Usage

1. Prepare Input Files:

- Place your meeting video file in the input directory (e.g., input/meeting.mkv).

2. Run the Application:

   ```bash
   python app.py
   ```

3. Output:

- Extracted audio will be saved in the output directory as meeting_audio.wav.
- Transcription will be saved as transcription.txt.
- Meeting minutes will be saved as meeting_minutes.md.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided that you include the original license.

## Acknowledgments

- FFmpeg for video-to-audio conversion.
- OpenAI's Whisper for speech-to-text transcription.
- Mistral AI for meeting minutes generation.
- The open-source community for their invaluable contributions.