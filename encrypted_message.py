import string

def load_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read().split()

def extract_keys(old_message_path, filler_words_path):
    old_message_words = set(load_file(old_message_path))
    filler_words = set(load_file(filler_words_path))
    
    keys = sorted(old_message_words - filler_words)
    
    print("Clés extraites (triées) :")
    for key in keys:
        print(key)
    
    letter_mapping = {}
    
    for i, key in enumerate(keys[:26]):
        letter_mapping[key] = string.ascii_uppercase[i]
    
    for i, key in enumerate(keys[26:36]):
        letter_mapping[key] = str(i)
    
    print("\nDictionnaire des clés :")
    for key, value in letter_mapping.items():
        print(f"{key} -> {value}")
    
    return letter_mapping

def decode_message(new_message_path, letter_mapping):
    encoded_words = load_file(new_message_path)
    decoded_message = ''
    unknown_words = []
    
    for word in encoded_words:
        if word in letter_mapping:
            decoded_message += letter_mapping[word]
        else:
            unknown_words.append(word)
            decoded_message += ''
    
    return decoded_message

old_message_path = 'ancien_message.txt'
filler_words_path = 'mots_de_remplissage.txt'
new_message_path = 'CASTELOOT Axel.txt'


letter_mapping = extract_keys(old_message_path, filler_words_path)
decoded_message = decode_message(new_message_path, letter_mapping)

print("\nMessage décodé :", decoded_message)