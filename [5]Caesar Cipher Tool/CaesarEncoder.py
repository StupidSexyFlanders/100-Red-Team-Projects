import sys

base_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

if len(sys.argv) != 3:
    print("Usage:  python3 CasesarEncoder.py '<message>' <switch>\n Please note that you message may not contain numbers and your switch should not be more than 25")
    exit()

message = str(sys.argv[1])
switch = int(sys.argv[2])

if switch > 25:
    print("Your switch may not be more than 25")
    exit()

uncoded = []
coded_msg_array = []

def encode(uncoded):
    for i in uncoded:
        if i == ' ':
            coded_msg_array.append(' ')
        else:
            i = (base_alphabet.index(i) + switch) % 26
            coded_msg_array.append(base_alphabet[i])

    coded_msg = ''.join(coded_msg_array)
    return coded_msg


for i in message:
    i = i.upper()
    uncoded.append(i)

encoded_message = encode(uncoded)
print("CAESAR CIPHER TEXT: " + encoded_message)

