from langdetect import DetectorFactory, detect

# ensures consistent probabilities from detect() method
DetectorFactory.seed = 0

def get_message_lang(message_text, user_target_lang, user_native_lang):
    if detect(message_text) == user_target_lang:
        return user_target_lang
    elif detect(message_text) == user_native_lang:
        return user_native_lang
    else:
        # Currently if a message has a number of spelling errors, the langdetect
        # library will possibly misidentify the language; i.e. "Helo Woorld"
        # will be misidentified as Dutch, rather than English. Returning the
        # entered message in this situation is just a placeholder until this
        # issue is resolved.
        return message_text