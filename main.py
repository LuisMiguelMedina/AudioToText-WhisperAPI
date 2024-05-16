import whisper
import markdown2
import os

# Cargar el modelo de Whisper
model = whisper.load_model("base")

# Ruta al archivo de audio
audio_file_path = "Luismi_2.wav"  # Asegúrate de reemplazar con la ruta correcta

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

    # Transcribir el archivo de audio
    result = model.transcribe(audio_file_path)

    # Obtener el texto de la transcripción
    transcription = result['text']

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
