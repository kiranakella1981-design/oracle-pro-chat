import streamlit as st

def pdf_uploader():
    """Create a file uploader for PDF documents."""
    return st.file_uploader(
        "Upload PDF Files",
        type="pdf",
        accept_multiple_files=True,
        help="Upload one or more PDF documents for processing."
        )
