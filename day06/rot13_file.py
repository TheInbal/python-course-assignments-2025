
input_string = "SHALOM HI"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Creating alphabet dict:
alphabet_dict = {}
rot_13_dict = {}
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]] = i + 1
    if (i + 1) <= 13:
        rot_13_dict[i + 1] = str(alphabet[i + 13])
    elif (i + 1) > 13:
        rot_13_dict[i + 1] = str(alphabet[i - 13])

# Convert action:
output_str = ""
for letter in input_string:
    if letter == " ":
        output_str = output_str + " "
    else:
        number = alphabet_dict[letter]
        conv_letter = rot_13_dict[number]
        output_str = output_str + conv_letter



print(output_str)
# print(alphabet_dict)
# print(rot_13_dict)
