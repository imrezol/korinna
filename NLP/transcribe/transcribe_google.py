import speech_recognition as sr
from pydub import AudioSegment
from os import path

file_name = "Transcribe1"
mp4_version = AudioSegment.from_file(path.expanduser("~/PycharmProjects/korinna/large_files/audio/" + file_name + ".m4a"), "mp4")
wav_version = path.expanduser("~/PycharmProjects/korinna/large_files/audio/" + file_name + ".wav")
print("Converting...",file_name)
mp4_version.export(wav_version, format="wav")
print("Conversion done")

print("Transcribing...",file_name)
# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(wav_version) as source:
    audio = r.record(source)  # read the entire audio file
    print("Transcription: " + r.recognize_google(audio))
print("Transcription done")
