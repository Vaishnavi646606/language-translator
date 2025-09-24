import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_text(text, target_language):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # ✅ using gpt-4.1-mini
        messages=[
            {"role": "system", "content": f"You are a translator. Translate the text into {target_language}."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.set_page_config(page_title="🌍 Language Translator", page_icon="🌐")
st.title("🌍 Language Translator Tool")
st.write("Translate text into multiple languages using **GPT-4.1-mini**")

# Input
text = st.text_area("Enter text to translate:")
languages = ["Hindi", "French", "Spanish", "German", "Japanese", "Chinese", "Arabic", "Russian"]
target_lang = st.selectbox("Select target language:", languages)

if st.button("Translate"):
    if text.strip():
        with st.spinner("Translating..."):
            translated = translate_text(text, target_lang)
        st.success(f"✅ Translated Text ({target_lang}):")
        st.write(translated)
    else:
        st.warning("⚠️ Please enter some text to translate.")

    #streamlit run app.py
