from pydub import AudioSegment
from pydub.utils import make_chunks
import os

def split_audio(audio_path, output_dir, chunk_duration_ms=15000):
    os.makedirs(output_dir, exist_ok=True)
    audio = AudioSegment.from_file(audio_path)
    chunks = make_chunks(audio, chunk_duration_ms)

    chunk_paths = []
    for i, chunk in enumerate(chunks):
        chunk_name = os.path.join(output_dir, f"chunk_{i}.wav")
        chunk.export(chunk_name, format="wav")
        chunk_paths.append(chunk_name)

    return chunk_paths
