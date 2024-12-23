from setuptools import setup, find_packages

# Reading long description from README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="minute_muse",  # The name of your project
    version="0.1.0",  # Version of your project
    author="Your Name",  # Your name or the name of the project maintainer
    author_email="your.email@example.com",  # Your contact email
    description="A tool for generating meeting minutes and action items from meeting transcriptions.",
    long_description=long_description,  # Detailed project description
    long_description_content_type="text/markdown",  # The format of long description (Markdown)
    url="https://github.com/yourusername/minute_muse",  # URL of your project repository
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=[  # External dependencies that your project requires
        "ffmpeg-python",  # For video/audio processing
        "pydub",  # For audio processing
        "whisper",  # For speech-to-text conversion
        "mistralai",  # For Mistral API client
        "python-dotenv",  # For managing environment variables
    ],
    classifiers=[  # Classifiers help others find your project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",  # Python version compatibility
    entry_points={  # Define command-line interfaces if any
        "console_scripts": [
            "minute_muse=minute_muse.app:main",  # Example CLI command
        ],
    },
)
