from google import genai
import os

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)