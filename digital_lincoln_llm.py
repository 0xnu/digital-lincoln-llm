import os
from openai import OpenAI
import PyPDF2
import io
import requests
import gradio as gr

class DigitalLincolnLLM:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.pdf_text = ""

    def load_pdf(self, pdf_path_or_url):
        if pdf_path_or_url.startswith("http"):
            # Download PDF from URL
            response = requests.get(pdf_path_or_url)
            pdf_file = io.BytesIO(response.content)
        else:
            # Open local PDF file
            pdf_file = open(pdf_path_or_url, 'rb')

        reader = PyPDF2.PdfReader(pdf_file)
        self.pdf_text = ""
        for page in reader.pages:
            self.pdf_text += page.extract_text()
        pdf_file.close()

    def chat(self, user_input):
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant that answers questions based on the provided PDF text. If the question cannot be answered based on the PDF text, simply respond with 'I'm sorry, but the answer to this question is not found in the provided PDF text.'"},
                {"role": "user", "content": f"PDF text:\n{self.pdf_text}\n\nQuestion: {user_input}"}
            ],
            max_tokens=150
        )
        assistant_response = chat_completion.choices[0].message.content.strip()
        return assistant_response

def chatbot_interface(api_key, pdf_path_or_url, user_input):
    chatbot = DigitalLincolnLLM(api_key)
    chatbot.load_pdf(pdf_path_or_url)
    response = chatbot.chat(user_input)
    return response

# Gradio UI Implementation
iface = gr.Interface(
    fn=chatbot_interface,
    inputs=[
        gr.Textbox(label="OpenAI API Key"),
        gr.Textbox(label="PDF Path or URL"),
        gr.Textbox(label="User Input")
    ],
    outputs=gr.Textbox(label="LLM Response"),
    title="Digital Lincoln LLM - 2024 Hackathon",
    description="Ask questions based on the content of a PDF document."
)
iface.launch()