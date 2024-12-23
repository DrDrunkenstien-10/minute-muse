import os

from audio.converter import convert_video_to_audio
from summarization.generator import generate_meeting_minutes
from transcription.splitter import split_audio
from transcription.transcriber import transcribe_audio_chunks
from utils.logger import setup_logging

# Setup logging
logger = setup_logging()

def main():
    logger.info("Starting MinuteMuse...")
    video_file = "input/meet_18_December_2024-2024-12-18_07.44.49.mkv"
    output_dir = "output"
    chunk_dir = os.path.join(output_dir, "chunks")
    transcription_file = os.path.join(output_dir, "transcription.txt")
    minutes_file = os.path.join(output_dir, "meeting_minutes.md")
    chunk_duration = 15 * 1000

    # Ensure output directories exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(chunk_dir, exist_ok=True)

    try:
        # Step 1: Convert video to audio
        audio_file = convert_video_to_audio(video_file, output_dir)

        # Step 2: Split the audio
        chunks = split_audio(audio_file, chunk_dir, chunk_duration)
        logger.info(f"Audio split into {len(chunks)} chunks.")

        # Step 3: Transcribe audio chunks
        transcription = transcribe_audio_chunks(chunks)
        with open(transcription_file, "w") as f:
            f.write(transcription)
        logger.info(f"Transcription saved to {transcription_file}.")

        # Step 4: Generate meeting minutes
        minutes = generate_meeting_minutes(transcription)
        with open(minutes_file, "w") as f:
            f.write(minutes)
        logger.info(f"Meeting minutes saved to {minutes_file}.")

    except (ValueError, FileNotFoundError, RuntimeError) as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
