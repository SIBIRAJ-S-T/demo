import os
import google.generativeai as genai

# Install the package (only works in Colab or a script with internet access)
try:
    import google.generativeai
except ModuleNotFoundError:
    os.system("pip install google-generativeai")

# Configure Gemini AI
genai.configure(api_key="AIzaSyCmrNE8Mb4U4xRWJzXG2rXzoU6W7SoWAwE")

def get_code(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
