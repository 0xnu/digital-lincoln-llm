import os
import PyPDF2
import io
import requests
import gradio as gr

class DigitalLincolnPDFChat:
    def __init__(self):
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
        # Convert user input and PDF text to lowercase for case-insensitive search
        user_input = user_input.lower()
        pdf_text_lower = self.pdf_text.lower()

        # Split the PDF text into sentences
        sentences = pdf_text_lower.split('. ')

        # Search for relevant sentences based on user input
        relevant_sentences = [sentence for sentence in sentences if user_input in sentence]

        if relevant_sentences:
            # Join the relevant sentences into a single response
            response = ' '.join(relevant_sentences)
        else:
            response = "I'm sorry, but the answer to this question is not found in the provided PDF text."

        return response

def chatbot_interface(pdf_path_or_url, user_input):
    chatbot = DigitalLincolnPDFChat()
    chatbot.load_pdf(pdf_path_or_url)
    response = chatbot.chat(user_input)
    return response

# Gradio UI Implementation
iface = gr.Interface(
    fn=chatbot_interface,
    inputs=[
        gr.Textbox(label="PDF Path or URL"),
        gr.Textbox(label="User Input")
    ],
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Digital Lincoln PDF Chat - 2024 Hackathon",
    description="Ask questions based on the content of a PDF document."
)

iface.launch()