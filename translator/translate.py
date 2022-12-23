from googletrans import Translator


def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='yo')
    return translation.text
