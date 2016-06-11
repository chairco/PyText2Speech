from text_to_speech.baidu import BaiduSpeech
from text_to_speech.watson import Watson


def get_speech(lang):

    lang = lang.lower()
    if lang in 'zh':
        speech_class = BaiduSpeech
    elif lang in ['ja', 'jp', 'it', 'en']:
        speech_class = Watson

    return speech_class