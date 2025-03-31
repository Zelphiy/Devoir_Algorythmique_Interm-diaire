import string

# Recherche les fichier et renvoie leur contenus
def load_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read().split()

# Extrait les clés 
def extract_keys(old_message_path, filler_words_path):
    old_message_words = set(load_file(old_message_path))
    filler_words = set(load_file(filler_words_path))
    
    # Permets de trier les clés dans l'ordre alphabétiques
    keys = sorted(old_message_words - filler_words)
    
    print("Clés extraites (triées) :")
    for key in keys:
        print(key)
    
    # Cré un dictionaire pour assigner les clés 
    letter_mapping = {}
    
    # Assigne les clés au lettres alphabétiques de A à Z
    for i, key in enumerate(keys[:26]):
        letter_mapping[key] = string.ascii_uppercase[i]
    
    # Assigne les clés au nombres de 0 à 9
    for i, key in enumerate(keys[26:36]):
        letter_mapping[key] = str(i)
    
    print("\nDictionnaire des clés :")
    for key, value in letter_mapping.items():
        print(f"{key} -> {value}")
    
    return letter_mapping

# Décode le message en utilisant le dictionaire 
def decode_message(new_message_path, letter_mapping):
    encoded_words = load_file(new_message_path)
    decoded_message = ''
    
    for word in encoded_words:
        if word in letter_mapping:
            # Si on croise un mot clé, on ajoute alors la lettre correspondante au message 
            decoded_message += letter_mapping[word]
        else:
            # Si on à un mot de remplissage inconu alors on l'ignore
            decoded_message += ''
    
    return decoded_message

# Définition des chemins des fichiers
old_message_path = 'ancien_message.txt'
filler_words_path = 'mots_de_remplissage.txt'
new_message_path = 'CASTELOOT Axel.txt'

# Execution
letter_mapping = extract_keys(old_message_path, filler_words_path)
decoded_message = decode_message(new_message_path, letter_mapping)

print("\nMessage décodé :", decoded_message)