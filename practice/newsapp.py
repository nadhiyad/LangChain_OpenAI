import streamlit as st
from langchain_config import llm_chain, extract_text_from_pdf, get_summary

st.title('News Tool')
st.write('Upload a PDF document containing news articles to get a summarized overview.')

# File uploader for PDF
uploaded_file = st.file_uploader('Upload your PDF file here', type='pdf')

# Define a specific file path
specific_file_path = '/Users/jagsanad/Desktop/python/Next hike/project 9/practice/TOI Delhi 23 Jul 2024.pdf'

if st.button('Get News'):
    if uploaded_file:
        # Save the uploaded PDF file with a dynamic name
        pdf_path = f"uploaded_{uploaded_file.name}"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Extract text from the uploaded PDF
        try:
            pdf_text = extract_text_from_pdf(pdf_path)
        except Exception as e:
            st.error(f"Error extracting text from PDF: {e}")
            st.stop()
        
        # Use the extracted text as the input for summarization
        summaries = get_summary(pdf_text)
        
        # Ensure `llm_chain.invoke` is correctly used
        try:
            response = llm_chain.invoke({'query': 'Summarize the following news articles', 'summaries': summaries})
            st.write('### Summary:')
            st.write(response)
        except Exception as e:
            st.error(f"Error generating summary: {e}")
    else:
        # Option to use a specific file if no file is uploaded
        try:
            pdf_text = extract_text_from_pdf(specific_file_path)
            summaries = get_summary(pdf_text)
            response = llm_chain.invoke({'query': 'Summarize the following news articles', 'summaries': summaries})
            st.write('### Summary:')
            st.write(response)
        except Exception as e:
            st.error(f"Error processing the specific file: {e}")