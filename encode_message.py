import string

# Get string such that there is no whitespace or punctuation
def strip_punctuations_and_whitespace(message):
    translator = str.maketrans('', '', string.punctuation) #Replaces punctuation with ''
    message = message.translate(translator)
    translator = str.maketrans('', '', string.whitespace) # Replaces whitespaces with ''
    message = message.translate(translator)
    return message.upper() # Convert to all uppercase

# Get a dictionary of Letters: Numbers pairs (A = 1, Z = 26)
def get_dictionary():
    num_to_alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alp_to_num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
    alp_num_dict = {}
    for i in range(0, 26):
        alp_num_dict[num_to_alph[i]] = alp_to_num[i]
    return alp_num_dict

# Turn message to numbers
def get_string_in_number_form(message):
    for i in range(0, len(message)):
        message[i] = alp_num_dict[message[i]]
    return message

# Get list in pairs of two 
# To encode the message two letters at a time
def arr_2_to_1(A):
    length = len(A)
    upper = int(len(A) / 2)
    if (length / 2) % 2 != 0:
        upper = int(length / 2)
        
    if length % 2 == 0:
        B = ['' for i in range(0, upper)]
    else:
        B = ['' for i in range(0, upper + 1)]
    for i in range(0, len(A)):
        if A[i] > 0 and A[i] < 10:
            A[i] = str('0') + str(A[i])
        if i == (len(A) - 1):
            B[int(i/2)] = str("00" + str(A[i]))
        if i % 2 != 0:
            B[int(i/2)] = str(A[i-1]) + str(A[i])
    return B

# Split decoded message back to letter pairs of 1
def arr_1_to_2(A):
    length = len(A)
    upper = length * 2
    B = ['' for i in range(0, upper)]
    for i in range(0, len(A)):
        string = A[i]
        B[i * 2] = string[0:2]
        B[i * 2 + 1] = string[2::]
    return B


# Get inverse of power from original function (naive method)
def get_mod_inverse(power, mod): # where power and mod are original power and mod
        power = power % mod
        for x in range(1, mod):
            if ((power * x) % mod == 1):
                return x 
        return 1
        

# Encode function
def f(x, power, mod):
    return pow(x, power) % mod

# Decode function
def g(x, inverse, mod):
    return pow(x, inverse) % mod

# Convert to string to iterate and change chars
string = strip_punctuations_and_whitespace(input("Input message to decode: "))
message = list(string)
print('Original: ', message)
original_message = list(string) # Copy of original message for later

# Get dictionary
alp_num_dict = get_dictionary()

# Get values from user
power = int(input("Enter power: "))
mod = int(input("Enter mod: "))

# Get string in number form
for i in range(0, len(message)):
    message[i] = alp_num_dict[message[i]]
    message[i] = int(message[i]) # Really turn it to numbers
print("Before encoded: ", message)

# Get list ready for encoding
message = arr_2_to_1(message)
print("Encoded: ", message)
for i in range(0, len(message)):
    message[i] = int(message[i])

# Encode 2 letters at a time
for i in range(0, len(message)):
    message[i] = f(message[i], power, mod)
# Make into string again to print
for i in range(0, len(message)):
    if message[i] < 1000 and message[i] > 99:
        message[i] = str('0') + str(message[i])
    elif message[i] < 100 and message[i] > 9:
        message[i] = str('00') + str(message[i])
    elif message[i] < 10:
        message[i] = str('000') + str(message[i])
    else:
        message[i] = str(message[i])
print("Coded: ", message)
# Make into int again
for i in range(0, len(message)):
    message[i] = int(message[i])

############################## SOMETHING WRONG WITH INVERSE (no negative values ??? ex 5(power), 11(mod))
# Get inverse
phi = mod - 1
inverse = get_mod_inverse(power, phi)

# Decode message
for i in range(0, len(message)):
    message[i] = g(message[i], inverse, mod)
# Make into string again
for i in range(0, len(message)):
    if message[i] < 1000 and message[i] > 99:
        message[i] = str('0') + str(message[i])
    elif message[i] < 100 and message[i] > 9:
        message[i] = str('00') + str(message[i])
    elif message[i] < 10:
        message[i] = str('000') + str(message[i])
    else:
        message[i] = str(message[i])
print('Decoded: ', message)


# Confirm it's the original message
message = arr_1_to_2(message) # Get each letters' numerical value
end_result = [message[i] for i in range(0, len(message)) if message[i] != '00'] # Remove 0's

values = list(alp_num_dict.values())
keys = list(alp_num_dict.keys())

for i in range(0, len(end_result)): # Get letter
    end_result[i] = keys[int(end_result[i]) - 1]

print('End result: ', end_result)
print('Original message: ', original_message)
#print(end_result == original_message)