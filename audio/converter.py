import ffmpeg
import os
import logging

# Constants
AUDIO_FORMAT = "wav"
AUDIO_CODEC = "pcm_s16le"
DEFAULT_AUDIO_FILENAME = "meeting_audio.wav"

# Configure logging
logger = logging.getLogger("MinuteMuse.AudioConverter")

def convert_video_to_audio(video_path: str, output_dir: str, audio_filename: str = DEFAULT_AUDIO_FILENAME) -> str:
    """
    Converts a video file to an audio file using FFmpeg and saves it in the specified output directory.

    :param video_path: Path to the input video file.
    :param output_dir: Directory to save the extracted audio file.
    :param audio_filename: Name of the audio file to be saved (default: "meeting_audio.wav").
    :return: Path to the saved audio file.
    :raises ValueError: If the video file or directory is invalid.
    :raises FileNotFoundError: If FFmpeg is not found.
    """
    if not os.path.isfile(video_path):
        raise ValueError(f"Video file {video_path} not found.")
    if not os.path.isdir(output_dir):
        raise ValueError(f"Output directory {output_dir} is invalid.")

    audio_filepath = os.path.join(output_dir, audio_filename)
    
    try:
        logger.info(f"Converting video '{video_path}' to audio.")
        ffmpeg.input(video_path).output(audio_filepath, acodec=AUDIO_CODEC).run()
        logger.info(f"Audio successfully saved to {audio_filepath}")
        return audio_filepath
    except ffmpeg.Error as e:
        logger.error(f"Error during FFmpeg processing: {e.stderr.decode()}")
        raise RuntimeError("FFmpeg encountered an error during processing.")
    except FileNotFoundError:
        logger.error("FFmpeg is not installed or not found in the system path.")
        raise FileNotFoundError("Ensure FFmpeg is installed and accessible in your system PATH.")
