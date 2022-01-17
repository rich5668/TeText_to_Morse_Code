# Dictionary representing the morse code
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                   ',': '__..__', "'": ".----.",

                   }

input_text = input('Hello, please input the message you would like to convert to morse code: ').upper()

morse_code_list = []

for char in input_text:
    if char != ' ':
        morse_code_list.append(MORSE_CODE_DICT[char])
    elif char == ' ':
        morse_code_list.append("/")

    morse_code_list.append(" ")

morse_code_string = ''.join(morse_code_list)
print(morse_code_string)
