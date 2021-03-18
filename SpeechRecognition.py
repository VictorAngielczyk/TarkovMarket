import speech_recognition as sr
import json

def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    # Google Cloud Speech-to-Text API
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = "None"
    with open('third-container-308014-1af2dffac850.json') as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.dumps(json.load(f), indent=2)

    textOut = ""
    try:
        textOut = str(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
        print("Output: " + textOut)
    except sr.UnknownValueError:
        print("Could not understand!")
    except sr.RequestError as e:
        print("Request failed; {0}".format(e))

    return textOut


# def textToSpeech():
    # Google Cloud Text-to-Speech API