import whisper
import markdown2
import os
import warnings
from pydub import AudioSegment
from tqdm import tqdm
import math

# Suprimir la advertencia específica
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Cargar el modelo de Whisper
model = whisper.load_model("base")

# Ruta al archivo de audio
audio_file_path = "./Audios/arturo_1.wav"  # Asegúrate de reemplazar con la ruta correcta

# Verificar si FFmpeg está en el PATH
ffmpeg_installed = os.system("ffmpeg -version") == 0
if not ffmpeg_installed:
    print("Error: FFmpeg no está instalado o no está en el PATH.")
    exit(1)

try:
    # Verificar la existencia del archivo de audio
    if not os.path.isfile(audio_file_path):
        raise FileNotFoundError(f"El archivo {audio_file_path} no se encontró.")

    print(f"Archivo de audio encontrado: {audio_file_path}")

    # Cargar el archivo de audio
    audio = AudioSegment.from_wav(audio_file_path)
    duration_ms = len(audio)  # Duración en milisegundos
    chunk_length_ms = 60000  # Longitud de cada fragmento en milisegundos (1 minuto)
    chunks = math.ceil(duration_ms / chunk_length_ms)  # Número de fragmentos

    print(f"Dividiendo el audio en {chunks} fragmentos de {chunk_length_ms/1000} segundos cada uno.")

    transcriptions = []
    for i in tqdm(range(chunks), desc="Transcribiendo"):
        start = i * chunk_length_ms
        end = min(start + chunk_length_ms, duration_ms)
        chunk = audio[start:end]

        # Guardar el fragmento temporalmente
        chunk_file_path = f"chunk_{i}.wav"
        chunk.export(chunk_file_path, format="wav")

        # Transcribir el fragmento
        result = model.transcribe(chunk_file_path)
        transcriptions.append(result['text'])

        # Eliminar el archivo de fragmento temporal
        os.remove(chunk_file_path)

    # Combinar todas las transcripciones
    transcription = " ".join(transcriptions)

    # Convertir la transcripción a formato Markdown
    md_content = f"# Transcripción del Audio\n\n{transcription}"

    # Guardar la transcripción en un archivo Markdown
    md_file_path = "transcripcion.md"
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Transcripción guardada en {md_file_path}")

except FileNotFoundError as e:
    print(f"Error: {e}. Asegúrate de que 'ffmpeg' esté instalado y en el PATH.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
