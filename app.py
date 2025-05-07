import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import time
import random
import pandas as pd

# -- Page Config --
st.set_page_config(page_title="Meta Ad Campaign Generator", page_icon="💡", layout="centered")

# -- Load Lottie Animation --
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

# -- Header UI --
st.title("🎯 Meta Ad Campaign Generator")
st.markdown("Generate professional Meta Ad Campaigns using **Groq + LLaMA 3** 💡")
st_lottie(lottie_ai, height=200, key="ai")
st.divider()

# -- User Inputs --
st.subheader("✍️ Enter Campaign Description")
prompt = st.text_area("Describe your campaign (e.g., target audience, budget, goals)", height=150)

st.subheader("📊 Select Campaign Metrics")
age_range = st.slider("Target Age Range", 18, 65, (25, 45))
daily_budget = st.slider("Daily Budget ($)", 100, 1000, 500, step=50)
duration_days = st.slider("Campaign Duration (days)", 7, 60, 30)

# -- Button + Glow Progress Animation --
if st.button("🚀 Generate Campaign"):
    if not prompt.strip():
        st.warning("Please enter campaign details above.")
    else:
        with st.spinner("✨ Generating campaign using LLaMA 3.3 70B..."):
            # Fake glowing loading bar
            for i in range(100):
                st.progress(i + 1, text="Glowing with ideas... 💡")
                time.sleep(0.01 + random.uniform(0, 0.01))

            # Call Groq API
            api_key = "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"
            endpoint = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "system", "content": "You are a professional Meta ad campaign generator."},
                    {"role": "user", "content": f"{prompt}\n\nAge Range: {age_range}\nDaily Budget: ${daily_budget}\nDuration: {duration_days} days"}
                ],
                "temperature": 0.7
            }

            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                data = response.json()
                campaign = data['choices'][0]['message']['content']
                st.success("✅ Campaign generated successfully!")

                # Show Campaign
                st.markdown("### 📢 Your Generated Campaign")
                st.markdown(campaign)

                # Budget Breakdown Chart
                st.markdown("### 💰 Budget Allocation")
                chart_data = pd.DataFrame({
                    "Platform": ["Facebook", "Instagram", "Audience Network"],
                    "Budget ($)": [
                        daily_budget * duration_days * 0.4,
                        daily_budget * duration_days * 0.3,
                        daily_budget * duration_days * 0.3,
                    ]
                })
                st.bar_chart(chart_data.set_index("Platform"))

            elif response.status_code == 401:
                st.error("❌ Invalid API Key. Please check your key.")
            elif response.status_code == 404:
                st.error("❌ Model not found. Double-check model name or access rights.")
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
