import speech_recognition as speech_recog

def speech_tr():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        print("Lütfen şimdi konuşun...")
        audio = recog.listen(audio_file)
        try:
            return recog.recognize_google(audio, language="tr-TR")
        except speech_recog.UnknownValueError:
            print("Ses anlaşılmadı, lütfen tekrar deneyin.")
            return ""
        except speech_recog.RequestError:
            print("Google servisinde bir sorun oluştu.")
            return ""

def speech_en():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        print("Please speak now...")
        audio = recog.listen(audio_file)
        try:
            return recog.recognize_google(audio, language="en-GB")
        except speech_recog.UnknownValueError:
            print("Sorry, I couldn't understand what you said. Please try again.")
            return ""
        except speech_recog.RequestError:
            print("Network error or Google service unavailable.")
            return ""
        

