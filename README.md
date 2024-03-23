## Digital Lincoln LLM - 2024 Hackathon

The Digital Lincoln PDF Chat is a Python-based chatbot that answers questions based on the content of a given PDF document. It extracts PDF text and uses OpenAI's GPT-3.5-turbo language model to generate contextually relevant responses to user queries. By integrating the extracted text from the PDF as context for the language model, the chatbot can provide informative and accurate answers based on the content of the PDF document.

### Features

- Extracts text from PDF documents, either from a local file or a URL
- Utilises OpenAI's GPT-3.5-turbo model to generate responses based on the retrieved information
- Provides a user-friendly web interface built with Gradio for easy interaction

### Requirements

To run the Digital Lincoln LLM, you need the following:

- Python 3.6 or higher
- OpenAI API key
- Required Python packages:
  - [openai](https://pypi.org/project/openai/)
  - [PyPDF2](https://pypi.org/project/pypdf/)
  - [requests](https://pypi.org/project/requests/)
  - [gradio](https://pypi.org/project/gradio/)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/0xnu/digital-lincoln-llm.git
   ```

2. Navigate to the project directory:

   ```
   cd digital-lincoln-llm
   ```

3. Install the required Python packages:

   ```
    ## Prerequisites
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    python3 -m pip install --upgrade pip
    deactivate
   ```

### Usage

1. Make sure you have an OpenAI API key. If you don't have one, sign up at [OpenAI](https://www.openai.com/) and create an API key.

2. Run the `digital_lincoln_llm.py` script:

   ```
   python3 digital_lincoln_llm.py
   ```

3. Open a web browser and go to `http://localhost:7860` to access the Digital Lincoln LLM interface.

4. Enter your OpenAI API key in the designated input field.

5. Provide the path to a local PDF file or a URL of a PDF document that you want to use as the knowledge base for the chatbot.

6. Start asking questions in the user input field, and the chatbot will generate responses by retrieving relevant information from the PDF, generating contextually appropriate answers using GPT-3.5-turbo.

🚨 FYI, it creates a `log.csv` file with sensitive information in the `flagged` folder.

### How It Works

When a user asks a question, the chatbot performs the following steps:

1. The question is used as a query to retrieve relevant passages from the extracted text of the PDF document.
2. The retrieved passages are then fed into the GPT-3.5-turbo model along with the user's question.
3. The language model generates a response based on the retrieved information, considering the context of the passages.
4. The generated response is returned to the user through the Gradio interface.

By incorporating a Large Language Model (LLM) into the process, the chatbot can focus on the most relevant information from the PDF document, leading to more accurate and contextually appropriate responses.

### Limitations

The accuracy and relevance of the chatbot's responses depend on the quality and content of the PDF document provided.
- The chatbot may be unable to answer questions that are not directly related to the information in the PDF.
- The chatbot's performance may be affected by the size and complexity of the PDF document.

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the [GitHub repository](https://github.com/0xnu/digital-lincoln-llm). Feel free to customise and expand the code based on your specific project details and requirements.

### License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgements

- [OpenAI](https://www.openai.com/) for providing the powerful GPT-3.5-turbo language model
- [PyPDF2](https://github.com/py-pdf/PyPDF2) for simplifying the extraction of text from PDF documents
- [Gradio](https://gradio.app/) for enabling the creation of interactive web interfaces

### Copyright

(c) 2024 [Finbarrs Oketunji](https://finbarrs.eu).

Developed at [LincolnHack 2024](https://2024.lincolnhack.org/) in collaboration with [Digital Lincoln](https://www.digitallincoln.co.uk/) — [Lincolnshire](https://en.wikipedia.org/wiki/Lincolnshire) 🇬🇧