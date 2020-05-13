import winsound
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
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
                    '(':'-.--.', ')':'-.--.-',' ':' | '} 

Morsecoded = ''
Message = input('Enter your message: ').upper()

for char in Message:
    if char in MORSE_CODE_DICT.keys():
        Morsecoded += MORSE_CODE_DICT[char] + ' '
        for code in MORSE_CODE_DICT[char]:
        	if code == ".":
        		winsound.Beep(2000, 75)
        	elif code == "-":
        		winsound.Beep(2000, 200)

        time.sleep(1)

print(f'Orginal: {Message}\nCoded: {Morsecoded}')
