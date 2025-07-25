from flask import Blueprint, request, render_template, send_from_directory, current_app
import os
import uuid

from audio.converter import convert_video_to_audio
from transcription.splitter import split_audio
from transcription.transcriber import transcribe_audio_chunks
from summarization.generator import generate_meeting_minutes
from .utils import allowed_file, get_file_type

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    minutes = None
    download_link = None
    error = None

    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            error = "No file selected."
            return render_template("index.html", error=error)

        if not allowed_file(file.filename):
            error = "Unsupported file format."
            return render_template("index.html", error=error)

        file_type = get_file_type(file.filename)
        unique_id = uuid.uuid4().hex
        filename = f"{unique_id}_{file.filename}"
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)

        try:
            if file_type == "video":
                audio_path = convert_video_to_audio(upload_path, current_app.config['OUTPUT_FOLDER'])
            elif file_type == "audio":
                audio_path = upload_path
            elif file_type == "transcript":
                with open(upload_path, "r") as f:
                    transcription = f.read()
                minutes = generate_meeting_minutes(transcription)
                minutes_path = os.path.join(current_app.config['OUTPUT_FOLDER'], f"minutes_{unique_id}.txt")
                with open(minutes_path, "w") as f:
                    f.write(minutes)
                download_link = f"/download/{os.path.basename(minutes_path)}"
                return render_template("index.html", minutes=minutes, download_link=download_link)

            # If audio, continue transcription and summarization
            chunk_dir = os.path.join(current_app.config['OUTPUT_FOLDER'], f"chunks_{unique_id}")
            os.makedirs(chunk_dir, exist_ok=True)

            chunks = split_audio(audio_path, chunk_dir)
            transcription = transcribe_audio_chunks(chunks)

            transcript_path = os.path.join(current_app.config['OUTPUT_FOLDER'], f"transcript_{unique_id}.txt")
            with open(transcript_path, "w") as f:
                f.write(transcription)

            minutes = generate_meeting_minutes(transcription)
            minutes_path = os.path.join(current_app.config['OUTPUT_FOLDER'], f"minutes_{unique_id}.txt")
            with open(minutes_path, "w") as f:
                f.write(minutes)

            download_link = f"/download/{os.path.basename(minutes_path)}"

        except Exception as e:
            error = f"An error occurred: {str(e)}"

    return render_template("index.html", minutes=minutes, download_link=download_link, error=error)

@main.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(current_app.config['OUTPUT_FOLDER'], filename, as_attachment=True)
