import streamlit as st
import PyPDF2
import io

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
        return None

def create_chat_completion(client, messages, model, pdf_text=None):
    """Create a chat completion using OpenRouter API"""
    try:
        system_message = """
        You are an AI assistant who is helpful, creative, clever, and very friendly.
        You aim to provide accurate and helpful responses while maintaining a positive
        and engaging conversation.
        """
        
        if pdf_text:
            system_message += """
            You have access to the content of a PDF document. Use this content to provide
            accurate answers to questions. If the question is about the PDF content,
            base your answer on the PDF. If the question is not related to the PDF,
            you can answer based on your general knowledge.
            
            PDF Content:
            """ + pdf_text

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                *messages
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None
