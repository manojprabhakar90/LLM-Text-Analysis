import streamlit as st
import openai

prompt = """
Your task is to convert the input text in English to other language
Identify the Sentiment of the text
Identify the Emotion expressed in the text
Identify the Important topics being conveyed in the sentence
Identify the Product name mentioned in the review.
Identify the Brand name mentioned in the review. 

"""

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

st.set_page_config(page_title="Template", page_icon=":robot:")
st.header("Text")

st.markdown("One Stop App for Identifying Sentiment, Emotion expressed, Brand discussed, Important Topics being discussed in the paragraph/sentence. This app also has a capability to convert English sentence to Local Language. Currently supports French, Tamil, German, Spanish, Malayalam and Telugu")

st.markdown("## Enter Your Sentence")


def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()
    
input_text = st.text_area(label="Input", label_visibility='collapsed')

language = st.selectbox('Which language would you like the text to be converted to',
        ('French','Spanish','Telugu','Tamil','Malayalam','German'))

if input_text:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    prompt = f"""Your task is to convert the ```{input_text}``` in English to ```{language}```"""
    response = get_completion(prompt)
    st.write(response)
    prompt = f"""
    Identify the following items from the Input text: 
    - Sentiment (positive or negative)
    - List of Emotions being expressed 
    - Determine five topics that are being discussed in the following text, which is delimited by triple backticks.
    - Company that made the item
    - Product being discussed

    Review text: '''{input_text}'''
    """
    response = get_completion(prompt)
    st.write(response)

st.markdown("Please raise a PR if you find something a miss. Thanks")