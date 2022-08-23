# This Script is used to convert from text to morse.

morse_alphabet = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def text_to_morse():   
    flag = 'y'
    morse = ''
    while flag == 'y':
        text = input('Please insert text to be converted into morse code: ' )
        text = text.upper()
        for x in text:
            if x != ' ':
                morse += morse_alphabet[x] + ' '
            else: 
                morse += ' '
        print(morse)
        flag = input('Would you like to continue? (y/n) ')


if __name__ == "__main__":
    text_to_morse()
