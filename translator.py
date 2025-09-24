import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_text(text, target_language):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # ✅ updated model
        messages=[
            {"role": "system", "content": f"You are a translator. Translate the text into {target_language}."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("🌍 Language Translator Tool (using gpt-4.1-mini)\n")
    text = input("Enter text to translate: ")
    lang = input("Enter target language (e.g., Hindi, French, Spanish): ")
    translated = translate_text(text, lang)
    print(f"\n✅ Translated Text ({lang}): {translated}")


#python translator.py