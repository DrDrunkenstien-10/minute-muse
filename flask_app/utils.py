import os

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4', 'mkv', 'wav', 'txt'}

def get_file_type(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    if ext in ['mp4', 'mkv']:
        return 'video'
    elif ext in ['wav']:
        return 'audio'
    elif ext in ['txt']:
        return 'transcript'
    return None
