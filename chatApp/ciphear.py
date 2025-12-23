emoji_cipher = {
    # Letters A–Z
    'A': '😀', 'B': '😂', 'C': '😅', 'D': '🤣', 'E': '😊',
    'F': '😍', 'G': '😎', 'H': '😏', 'I': '😒', 'J': '😞',
    'K': '😔', 'L': '😢', 'M': '😭', 'N': '😡', 'O': '😱',
    'P': '😴', 'Q': '🤓', 'R': '🤔', 'S': '🤩', 'T': '🤗',
    'U': '🤨', 'V': '😇', 'W': '🙃', 'X': '😉', 'Y': '😋', 'Z': '😜',

    # Numbers 0–9
    # Numbers 0–9 (simple single emojis)
    '0': '🔟', '1': '🥇', '2': '🥈', '3': '🥉', '4': '🏅',
    '5': '🎖', '6': '🏆', '7': '🎯', '8': '🎲', '9': '🎮',

    # Common symbols
    ' ': '⬜', '.': '⚫', ',': '⚪', '?': '❓', '!': '❗'
}

emoji_binary = {
    '😀': '00000', '😂': '00001', '😅': '00010', '🤣': '00011', '😊': '00100',
    '😍': '00101', '😎': '00110', '😏': '00111', '😒': '01000', '😞': '01001',
    '😔': '01010', '😢': '01011', '😭': '01100', '😡': '01101', '😱': '01110',
    '😴': '01111', '🤓': '10000', '🤔': '10001', '🤩': '10010', '🤗': '10011',
    '🤨': '10100', '😇': '10101', '🙃': '10110', '😉': '10111', '😋': '11000',
    '😜': '11001',
    
     # Numbers
    '🔟': '11010', '🥇': '11011', '🥈': '11100', '🥉': '11101', '🏅': '11110',
    '🎖': '11111', '🏆': '00000', '🎯': '00001', '🎲': '00010', '🎮': '00011',
    
    '⬜': '00100', '⚫': '00101', '⚪': '00110', '❓': '00111', '❗': '01000'
}

def encrypt_msg(msg):
    msg=msg.upper()
    newstr=""
    for ch in msg:
        if ch in emoji_cipher:
            newstr+=emoji_cipher[ch]

        else:
            newstr+=ch

    return newstr
       
def encrypt_to_binary(encrypted_msg):
    binarystr=""
    for i in encrypted_msg:
        if i in emoji_binary:
            binarystr+=emoji_binary[i]

        else:
            binarystr+=i

    return binarystr

text = "my name is akshay"
emoji_encrypted = encrypt_msg(text)
binary_encoded = encrypt_to_binary(emoji_encrypted)

print("Original:", text)
print("Emoji Layer:", emoji_encrypted)
print("Binary Layer:", binary_encoded)\


# Reverse dictionaries
binary_emoji = {v: k for k, v in emoji_binary.items()}
emoji_text = {v: k for k, v in emoji_cipher.items()}

def decrypt_from_binary(binary_msg):
    chunks = [binary_msg[i:i+5] for i in range(0, len(binary_msg), 5)]
    emoji_str = ""
    for chunk in chunks:
        emoji_str += binary_emoji.get(chunk, '?')
    return emoji_str

def decrypt_msg(emoji_str):
    text = ""
    for emoji in emoji_str:
        text += emoji_text.get(emoji, '?')
    return text

