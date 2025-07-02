import argostranslate.package
import argostranslate.translate

def translate_text(text, lang_code):
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = next((l for l in installed_languages if l.code == "en"), None)
    to_lang = next((l for l in installed_languages if l.code == lang_code), None)

    if from_lang and to_lang:
        translation = from_lang.get_translation(to_lang)
        return translation.translate(text)
    return text
