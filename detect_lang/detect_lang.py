from langdetect import DetectorFactory, detect, detect_langs
import time

def get_message_lang(message_text, user_target_lang, user_native_lang):
    try:
        # return target lang if message is target lang
        if detect(message_text) == user_target_lang:
            return user_target_lang

        # return native lang if message is native lang
        elif detect(message_text) == user_native_lang:
            return user_native_lang

        # if native/target lang is not detected (due to langdetect probability algorithm) then generate new probabilities
        # until native/target lang is detected
        else:
            init_time = time.time()
            while True:
                # if native/target lang is not detected after five seconds, return None
                if (time.time()-init_time) >= 5:
                    return None
                prob_list = detect_langs(message_text)
                for item in prob_list:
                    if item.lang == user_target_lang or item.lang == user_native_lang:
                        return item.lang
    except:
        return None
