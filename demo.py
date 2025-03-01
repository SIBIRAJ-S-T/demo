import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyCmrNE8Mb4U4xRWJzXG2rXzoU6W7SoWAwE")

# Function to get AI-generated code
def get_code(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text  # Returns the generated code as text
