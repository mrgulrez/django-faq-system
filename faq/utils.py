from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang):
    translation = translator.translate(text, dest=dest_lang)
    return translation.text