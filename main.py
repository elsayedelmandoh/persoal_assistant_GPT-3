# + **Personal Assistant using OpenAI GPT-3 model**

# + **Function to convert text to speech**
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def text_to_speech(text):
    '''
    - set speed audio value 125 
    - Takes a text input from function recognize_speech_from_microphone,
    - Converts text to speech using the 'pyttsx3'
    '''
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

# + **Function to process microphone input**
import speech_recognition as sr

# Initialize the speech recognition engine
r = sr.Recognizer()
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


# + **Function to process text input**
def process_text_input():
    text = st.text_input("Enter text:")
    return text


# + **Function to interact with GPT-3**
import openai

# Set up your OpenAI API key
openai.api_key = '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'

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

# '''
# {
#   "choices": [
#     {
#       "finish_reason": "length",
#       "index": 0,
#       "logprobs": null,
#       "text": " Where are you from? and you know, the normal stuff when you meet someone new. She didn really answer me and I started to get the feeling that she was really weird.\n\n\u201cAre you a real person?\u201d\n\nWe talked for a little while and then I asked her if she wanted to see a picture of me with my mouth open and she said yes. So I sent it. The next time I went to talk to her, she"
#     }
#   ],
#   "created": 1684967071,
#   "id": "cmpl-7JrCBNzoiap5wHpn8wMcENQZMNMf3",
#   "model": "davinci",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 100,
#     "prompt_tokens": 6,
#     "total_tokens": 106
#   }
# }
# '''

# + **Build GUI**
import streamlit as st


# + **Main function**
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

# + **Run the main function**
if __name__ == "__main__":
    main()