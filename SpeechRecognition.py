import speech_recognition as sr
import json
import pyaudio
from gtts import gTTS
import os
from playsound import playsound

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "third-container-308014",
  "private_key_id": "1af2dffac850e9c444f6401f4e03a2fa830d31f0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDJ851wsxmD1TxR\nhB6408/AC7EtA15nUVOF4Hgzz09u1zkUEovZYGZmjE/dQ51CsAPWadBMql/7aXup\n/B9c+XVVp0CaA7TtMYg9Q8FSYAVrx2qS4Fqob3NrwHGDNQ+6sdRlWpjb3MiXR+Lk\nWyVYykQhg190Mp81imXvCuEh1vjV1PC2JN4vG57RzVLJFOrd7qz9wAiucE2B9yuE\n54lsiU0wnpbTM93q+Ldlq0br+W1XTA4TxZb3QAl9nGfBjCG5A5QXqqHT2BM694ML\nGp5BkMlUB+zgdPIF63lNIRYJ9lQq9o1TRH/f+8/WhjSGP8XPwBqOivAHt9Tz0zvY\nN+TUo6N/AgMBAAECggEACFtkcH142NPCIz1saAmb1z6knlA9X9kls6yOTNaPWu7d\nFc+OqfgrRKMZyvY5U8Ek54KJdCK4xhafX3Fnetl32YuKSNVOb2JVWPOs1FPU5Zji\n+CEAn2e9RwA3sk5H0Fn7iBYvrSl9w4TeBsUezoXQO/LLyGsv229WuIWiu1vCAFc0\nq6B88aFVJtx8VHh/C65oWRNEqvPRNJ5WYXnd9oJVfESBfDArDXsUNHlGV/XLrTQC\nsxw7n2qM4xyG7hdS8KLhJpG1tnoWeOpTRzS8NZsoO23fU9Onc2/xzRFGfIh94Z3F\nCZRn6yWt71Jo3n5I+byZPh/Ms9/1oPmzCuQV+EjkgQKBgQDpeN3GhbRxdxCizPA0\nmZqIMXqzKEb6uvlkY+F+T7gNn4tvJ18Hi1YQb2kf3p2V8dsR/vshfGejcFpRLSuQ\nvXK5w+UgykTEpdbcMxIFgHGDXcxdqA85IunPkw7XTUctv33w9ZMrr/nyNr0R8iq0\np2YAm7zgRl1HXGvIkL1p+l6KxwKBgQDdcCRNFAspj3GgCUffaA/MfiXUjy12OpME\nUJNPy/yrr9k4OCKw1l9Im+B4fj4L+XuQ7mDbFRIj0XeDE2jGmlsRUTxqXWrQ8S6a\nneKEJN0F6BBBRzgaY3Duuok5qGQpPdEXhNMrc3GHEEW4A+0X87g3JIwYeGsGVEIR\nbhLxACKpiQKBgQCEMRZJGF1RvVujAiyja7FOmc1icVS3FHSuvcroTNTmicZWGlG5\nINCLH7nC/LX3N2iVqOyiSiEYLj5FJjE7k7jIq70pMr17JncgWJ5ElTQwcESNZuGv\ntS/zgs1tZGj/4yO48iLxIoN//DRTW+2IOhwMDiIETnL0O8UfW6yTu9oZ8wKBgCry\nwCeu9odGCgy3IBiFj2LjKKU0a+XdcHxKwHeeodAO2DueL6RKv8pOaVgVbCVYaw3u\nHhz/1jfaParPjefPMlCGiAg9PCVwUdCtRKzKlY+6tcRjcs8zcEjtJwZm0Z5qHe7I\n1Ug9KMzAbDVHlamqnJUdYoqweFmO6A2HYucZVp+5AoGAehjkKLR77NrmE3zQ4QBH\nCkB7E1cAib1B7rWwjZ9jdIiR3+NAqP8LpHjuz++n2Qs62VrSgKG4wJRzUrsaFSbV\n9+thTwL2bUdr+bI+VdovKrsf6L4Ar2e0cbbJ3MDoBC2YZAucdb7Wu0EvJ+25Gwjh\nb/K3ndNHRMI99BM7NizuMwM=\n-----END PRIVATE KEY-----\n",
  "client_email": "robert@third-container-308014.iam.gserviceaccount.com",
  "client_id": "114207626985815442103",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/robert%40third-container-308014.iam.gserviceaccount.com"
}"""


def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSay something!")
        audio = r.listen(source)

    # GOOGLE_CLOUD_SPEECH_CREDENTIALS = "None"
    # with open('third-container-308014-1af2dffac850.json') as f:
    #     GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.dumps(json.load(f), indent=2)

    # Google Cloud Speech-to-Text API
    textOut = ""
    try:
        textOut = str(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
        print("Output: " + textOut)
    except sr.UnknownValueError:
        print("Could not understand!")
        return None
    except sr.RequestError as e:
        print("Request failed; {0}".format(e))

    return textOut


def textToSpeech(text):
    tts = gTTS(text=text, lang="en", slow=False)
    os.remove("voice.mp3")
    tts.save("voice.mp3")

    playsound("voice.mp3")


if __name__ == "__main__":
    textToSpeech(speechToText())