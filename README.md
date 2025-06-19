# An-AI-Integrated-System-for-Multi-Image-X-Ray-and-MRI-Scan-Analysis-Using-GEN-AI

## Overview
This project is an AI-powered medical imaging analyzer built using **Google Gemini API**, **Streamlit**, and **PIL**. It allows users to upload multiple **X-ray** or **MRI scans**, detect abnormalities using generative AI, and receive possible recovery suggestions based on the scans.


## Features
- **Multi-image support**: Upload and analyze multiple scans at once  
- **Abnormality detection**: Identifies fractures, tumors, infections, etc.  
- **Recovery guidance**: Provides AI-generated recovery suggestions  
- **Streamlit interface**: Interactive and user-friendly web app  
- **Gemini 1.5 Flash model**: Fast, context-aware radiology analysis  

## Installation
To set up the project locally, follow these steps:

1. 1. **Clone the repository**  
   ```bash
   git clone https://github.com/Rajesh830/ai-medical-analyzer.git
   cd ai-medical-analyzer
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your environment
   ```sh
   Create a .env file in the root directory
   Add your Google API key:
   GOOGLE_API_KEY=your_google_api_key_here
   ```
4.Run the Streamlit app
     streamlit run app.py   

## Usage
1. **Upload multiple X-ray or MRI images (formats: JPG, PNG).**
2. **For each image, select whether it is an X-ray or MRI.**
3. **Click "Analyze Scans" to detect abnormalities.**
4. **Click "Provide Recovery Suggestions" to get treatment advice.**


## Requirements
- **Python 3.x**
- **Streamlit** (Web app framework)
- **Pillow (PIL)** (Image handling) 
- **google-generativeai** (Gemini model API)
- **python-dotenv** (For managing API keys)
- **Other dependencies listed in requirements.txt** 

-Sample Output:

**Uploaded Image**: chest_scan.jpg
**Selected Type**: X-ray
**Analysis**:

"Mild left lower lobe infiltrates consistent with early pneumonia. No evidence of fractures or masses."

**Recovery Suggestions**:

"Consider antibiotics and follow-up imaging in 5-7 days. Maintain hydration and avoid smoking or allergens during recovery."


