# Audio Transcription Project

## Requirements

Make sure you have the following packages installed:

```bash
pip install whisper markdown2 pydub tqdm
```

Additionally, you need to have [FFmpeg](https://ffmpeg.org/download.html) installed and available in your PATH.

## Usage

### Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

2. **Install the dependencies:**

```bash
pip install whisper markdown2 pydub tqdm
```

3. **Ensure FFmpeg is installed:**

Check if FFmpeg is in the PATH by running:

```bash
ffmpeg -version
```

If FFmpeg is not installed, follow the instructions on [FFmpeg](https://ffmpeg.org/download.html) to install it.

4. **Place your audio file in the specified path:**

By default, the audio file should be in `./Audios/audio.wav`. Make sure to update `audio_file_path` in the script if your audio file is in a different location.

5. **Run the script:**

```bash
python transcribe.py
```