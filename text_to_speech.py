def text_to_speech(text, lang_code):
    output_file = "translated_audio.mp3"
    os.system(f'espeak-ng -v {lang_code} "{text}" -w {output_file}')
    return output_file
