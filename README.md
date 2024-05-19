# Audio Transcription Project

## Requisitos

Asegúrate de tener los siguientes paquetes instalados:

```bash
pip install whisper markdown2 pydub tqdm
```

Además, necesitas tener [FFmpeg](https://ffmpeg.org/download.html) instalado y disponible en tu PATH.

## Uso

### Instrucciones

1. **Clona el repositorio:**

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. **Instala las dependencias:**

```bash
pip install whisper markdown2 pydub tqdm
```

3. **Asegúrate de que FFmpeg esté instalado:**

Verifica si FFmpeg está en el PATH ejecutando:

```bash
ffmpeg -version
```

Si FFmpeg no está instalado, sigue las instrucciones en [FFmpeg](https://ffmpeg.org/download.html) para instalarlo.

4. **Coloca tu archivo de audio en la ruta especificada:**

Por defecto, el archivo de audio debe estar en `./Audios/audio.wav`. Asegúrate de actualizar `audio_file_path` en el script si tu archivo de audio está en una ubicación diferente.

5. **Ejecuta el script:**

```bash
python transcribe.py
```