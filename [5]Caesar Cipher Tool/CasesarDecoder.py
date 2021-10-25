import sys

base_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

if len(sys.argv) != 3:
    print("Usage:  python3 CasesarDecoder.py '<message>' <switch>\n Please note that you message may not contain numbers and your switch should not be more than 25")
    exit()

message = str(sys.argv[1])
switch = int(sys.argv[2])

if switch > 25:
    print("Your switch may not be more than 25")
    exit()


coded = []
decoded_msg_array = []

def decode(coded):
    for i in coded:
        if i == ' ':
            decoded_msg_array.append(' ')
        else:
            i = (base_alphabet.index(i) - switch) % 26
            decoded_msg_array.append(base_alphabet[i])

    decoded_msg = ''.join(decoded_msg_array)
    return decoded_msg

for i in message:
    i = i.upper()
    coded.append(i)

decoded_message = decode(coded)
print("CAESAR CIPHER TEXT: " + decoded_message)

