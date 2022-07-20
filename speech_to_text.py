import speech_recognition as sr

def speech_to_text(audioPath: str, language: str = "en-US"): 
    r = sr.Recognizer()
    with sr.AudioFile(audioPath) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            print('Converting audio transcripts into text ...')
            return text
        except:
            return "Could not convert the speech"