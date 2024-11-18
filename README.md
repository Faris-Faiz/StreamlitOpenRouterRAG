# OpenRouter PDF ChatBot 🤖📄

A Streamlit-powered chatbot application that provides interactive conversational capabilities with OpenRouter AI and PDF document chat support.

## Features ✨

- 🌐 OpenRouter AI Integration
- 📄 PDF Document Chat
- 🔑 Customizable AI Model Selection
- 💬 Interactive Chat Interface

## Prerequisites 📋

Before you begin, ensure you have the following installed on your Windows system:
- [Python 3.12.7](https://www.python.org/downloads/release/python-3127/) (recommended version)
- [Git](https://git-scm.com/downloads) (for cloning the repository)
- [OpenRouter API Key](https://openrouter.ai/) (required for AI interactions)

## Installation Guide 🚀

Follow these steps to set up the project locally on your Windows machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/OpenRouterChatBotStreamlit.git
cd OpenRouterChatBotStreamlit
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to avoid any conflicts with other Python projects:

```bash
# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application 🎯

Once you've completed the installation, you can run the application:

```bash
streamlit run app.py
```

## How to Use 🖥️

1. Enter your OpenRouter API key in the sidebar
2. (Optional) Select a specific AI model
3. Upload a PDF document (if you want to chat about its contents)
4. Start chatting with the AI!

### PDF Chat Functionality

- Upload a PDF in the sidebar
- Ask questions about the document's content
- Clear PDF or chat history as needed

## Supported Features

- Multiple AI model support
- PDF text extraction and context-aware responses
- Flexible chat interface
- Easy model and API key configuration

## Troubleshooting 🔧

1. Ensure Python 3.12.7 is properly installed:
   ```bash
   python --version
   ```

2. Verify that your virtual environment is activated

3. If you face dependency issues:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

## Requirements

- Streamlit
- OpenAI Python Library
- PyPDF2

## License 📄

This project is licensed under the MIT License.

## Contributing 🤝

Contributions, issues, and feature requests are welcome!

## Contact 📧

Created by Faris Faiz - feel free to connect!
