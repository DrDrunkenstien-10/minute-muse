import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def generate_meeting_minutes(transcription):
    # Ensure that the API key is loaded properly
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please check your .env file.")

    # Initialize the Mistral client
    client = Mistral(api_key=api_key)
    model = "mistral-large-latest"

    prompt = f"""
    You are a professional meeting minutes generator. Your task is to summarize the following transcription and generate action items.

    # Transcription:
    {transcription}

    ## Output:
    """
    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
