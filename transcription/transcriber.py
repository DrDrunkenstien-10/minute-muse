import whisper

def transcribe_audio_chunks(chunks, model_size="small"):
    model = whisper.load_model(model_size)
    transcripts = []

    for chunk_path in chunks:
        audio = whisper.load_audio(chunk_path)
        audio = whisper.pad_or_trim(audio)
        result = model.transcribe(audio)
        transcripts.append(result["text"])

    return "\n".join(transcripts)
