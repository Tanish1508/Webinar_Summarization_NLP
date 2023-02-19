import requests
from api_02 import *

filename = r"D:\NLP_RI\converted_audio.wav"
audio_url = upload(filename)

save_transcript(audio_url, 'output1')