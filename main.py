# + **Personal Assistant using OpenAI GPT-3 model**

import pyttsx3
import openai
import streamlit as st
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()
openai.api_key = 'your_api_key'

def text_to_speech(text):
    '''
    - set speed audio value 125 
    - Takes a text input from function recognize_speech_from_microphone,
    - Converts text to speech using the 'pyttsx3'
    '''
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def process_speech_input():
    '''
    - Records audio from the microphone, "listen"
    - Converts audio to text using Google's speech recognition service, "recognize_google"
    -  Returns the recognized text.
    '''
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
        return ""
    except sr.RequestError as e:    
        print("Could not request results from Google Speech Recognition service.")
    return ""

def process_text_input():
    text = st.text_input("Enter text:")
    return text


def process_input_with_gpt3(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,# maximum number of tokens in the response.
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    st.title("Speech Recognition with GPT-3")
    
    input_method = st.selectbox("Select input method:", ("Speech (Microphone)", "Text"))
    if input_method == "Speech (Microphone)":
        input_text = process_speech_input()
    else:
        input_text = process_text_input()

    if input_text:
        output_text = process_input_with_gpt3(input_text)

        st.subheader("Output:")
        st.write(output_text)
        st.audio(text_to_speech(output_text))

if __name__ == "__main__":
    main()
