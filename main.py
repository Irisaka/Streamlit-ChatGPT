import streamlit as st
import openai

openai.api_key = st.secrets["API_KEY"]

def main():
    st.set_page_config(
        page_title="Translator",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    st.title("Use OpenAI to translate")

    # Define the source text to translate
    st.header("Input")
    source_text = st.text_area("Text to translate")
    # Define the target language (e.g. "zh" for Chinese, "en" for English, "ja" for Japanese)
    target_language = st.selectbox("Target language", ["zh", "en", "jp"])
    prompt = f"translate {source_text} to {target_language}"
    model = "text-davinci-003"
    temperature = st.slider("Choose the temperature:", 0.0, 1.0, 0.5)

    if st.button("Translate -->"):
        # Use the OpenAI API to translate the source text to the target language
        translated_text = generate_translated_result(prompt, model, temperature)
        st.success("Finished!")
        st.header("Output")
        st.write(translated_text)
    else:
        st.header("Output")
        st.write("Waiting for your input")

def generate_translated_result(prompt, model, temperature):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=temperature,
    )
    # Extract the translated text from the API response
    translated_text = response["choices"][0]["text"]
    return translated_text

if __name__ == "__main__":
    main()