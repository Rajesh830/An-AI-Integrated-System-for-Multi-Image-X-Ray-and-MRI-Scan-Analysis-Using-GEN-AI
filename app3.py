### AI-Powered X-Ray & MRI Scan Analyzer with Multi-Image Support
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to process medical images with Gemini AI
def analyze_medical_image(image_data, image_type):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"You are a radiology expert. Analyze this {image_type} scan and detect any abnormalities such as fractures, tumors, infections, or degenerative diseases."
        response = model.generate_content([prompt, image_data[0]])
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Function to provide recovery suggestions
def get_recovery_suggestions(image_data, image_type):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"You are a medical expert. Based on this {image_type} scan, provide possible recovery options, treatments, and lifestyle changes for the detected condition."
        response = model.generate_content([prompt, image_data[0]])
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Function to convert image to API-compatible format
def prepare_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": bytes_data}]
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="AI X-Ray & MRI Analyzer 🏥")

st.title("🏥 AI X-Ray & MRI Scan Detector")
st.write("Upload X-ray and MRI images to detect abnormalities and get recovery suggestions.")

uploaded_files = st.file_uploader("Choose X-ray & MRI images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    image_data_list = []
    image_types = []

    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)
        
        image_data = prepare_image(uploaded_file)
        if image_data:
            image_data_list.append(image_data)
            # Asking user to classify image type
            image_type = st.selectbox(f"Select type for {uploaded_file.name}", ["X-ray", "MRI"], key=uploaded_file.name)
            image_types.append(image_type)

    if st.button("Analyze Scans"):
        st.subheader("AI Analysis Results:")
        for idx, image_data in enumerate(image_data_list):
            with st.spinner(f"Analyzing {image_types[idx]} scan..."):
                response = analyze_medical_image(image_data, image_types[idx])
                st.write(f"{image_types[idx]} Analysis for {uploaded_files[idx].name}:")
                st.write(response)

    if st.button("Provide Recovery Suggestions"):
        st.subheader("AI Recovery Suggestions:")
        for idx, image_data in enumerate(image_data_list):
            with st.spinner(f"Generating recovery suggestions for {image_types[idx]} scan..."):
                recovery_response = get_recovery_suggestions(image_data, image_types[idx])
                st.write(f"*Recovery Suggestions for {uploaded_files[idx].name} ({image_types[idx]} Scan):*")
                st.write(recovery_response)