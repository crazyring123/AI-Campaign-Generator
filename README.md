# AI Campaign Generator

## Overview
The **AI Campaign Generator** is a powerful application built using Streamlit and Groq's LLaMA model to generate professional Meta ad campaigns based on user inputs. The app allows users to create ad campaigns by providing details such as target audience, goals, and budget.

This project showcases the integration of machine learning with a user-friendly web interface to streamline the ad creation process. It uses Groq and LLaMA 3.3-70B to generate ad content that aligns with the campaign goals.

## Features
- **Streamlit-based Interactive UI**: User-friendly web interface with sliders, graphs, and animations.
- **AI-Powered Campaign Generation**: Integrates Groq API with the LLaMA model to generate Meta ad campaigns.
- **Responsive Design**: Mobile-friendly and clean interface.
- **Real-time Feedback**: See results instantly upon entering campaign details.
  
## Installation Instructions

### Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/crazyring123/AI-Campaign-Generator.git
cd AI-Campaign-Generator
Set up Virtual Environment (Optional but Recommended)
Create and activate a Python virtual environment:

bash
Copy
Edit
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
Install Dependencies
Once your virtual environment is active, install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit App
To launch the app, run the following command:

bash
Copy
Edit
streamlit run app.py
The app will open in your browser, and you can start generating campaigns!

Usage
Campaign Generation
Enter Campaign Details: Input details such as target audience, budget, and goals.

Generate Campaign: Click the button to generate your Meta ad campaign.

View Generated Campaign: The campaign details will be displayed, including ad copy, placements, and strategies.

Features
Interactive Sliders: Adjust budget, audience age range, and other settings with real-time feedback.

Graphs & Animations: Visual representations of campaign data for a better understanding.

Lottie Animations: Dynamic animations to enhance the UI experience.

Deployment
Deploy on Streamlit Cloud
Sign up for Streamlit Cloud (https://share.streamlit.io/).

Push your changes to GitHub.

Link your GitHub repository with Streamlit Cloud.

Your app will automatically deploy on Streamlit Cloud.

Deploy Locally
Clone the repository and set up a virtual environment.

Install dependencies as mentioned in the Installation section.

Run the Streamlit app locally.

API Integration
This app uses the Groq API for campaign generation. Make sure you replace your API key in the application with the key you obtained from Groq.

python
Copy
Edit
API_KEY = "your_groq_api_key_here"
Project Structure
app.py: Main Streamlit app that handles UI and logic.

requirements.txt: Lists all the dependencies for the project.

README.md: This documentation file.

assets/: Folder containing static assets like images and Lottie JSON files for animations.

Dependencies
The project uses the following Python packages:

streamlit

requests

streamlit_lottie

(Other necessary libraries listed in requirements.txt)

You can install them via the following:

bash
Copy
Edit
pip install -r requirements.txt
Credits
Groq: AI model for campaign generation.

LLaMA 3.3-70B: Language model for generating ad copy.

Streamlit: Framework for building the web app.

Known Issues
The app currently requires a valid Groq API key to generate campaigns. Ensure the API key is configured before running the app.

The model name used in the app may change, so please ensure that the Groq API is updated accordingly.

Future Enhancements
Add more customization options for the campaign (e.g., multi-language support, more targeting parameters).

Integration with additional ad platforms (e.g., Google Ads, Twitter Ads).

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy
Edit

### Key Sections in the Template:
1. **Overview**: Briefly explains the app’s functionality.
2. **Features**: Lists key features of the app.
3. **Installation Instructions**: Step-by-step guide for setting up the app locally.
4. **Usage**: How to use the app for generating ad campaigns.
5. **Deployment**: Guides for deploying the app on Streamlit Cloud or running it locally.
6. **API Integration**: Explanation for integrating the Groq API key.
7. **Project Structure**: Describes the file and folder structure of the project.
8. **Dependencies**: Lists the Python dependencies used in the project.
9. **Credits**: Gives credit to external libraries and APIs used.
10. **Known Issues and Future Enhancements**: Any current issues or planned improvements.

---

### Final Notes:
- Replace `your_groq_api_key_here` with your actual Groq API key when using the app.
- Ensure that the URL for your GitHub repository is correct before sharing it.

This should now give you a clean, comprehensive README for your project! 🎉











Search

Reason

Deep research

Create image



ChatGPT can make mistakes. Check important info. See Cookie Preferences.
