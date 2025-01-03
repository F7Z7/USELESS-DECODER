def decoder(input_string, length):
    encoded_string = ""
    #below arer the strings made for reference
    up_ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low_ref = "abcdefghiklmnopqrstuvwxyz"
    for i in range(length):
        if (i + 1) % 2 == 0:#chechk if the index is even logically,if even the lettetr is shifted forwaded once
            if input_string[i].isupper():
                for j, letter in enumerate(up_ref):
                    if input_string[i] == letter:
                        encoded_string += up_ref[(j + 1) % 26]
                        break
            elif input_string[i].islower():
                for j, letter in enumerate(low_ref):
                    if input_string[i] == letter:
                        encoded_string += low_ref[(j + 1) % 26]
                        break
        else:#else the index is odd logically and lettetr is shifted backwards once
            if input_string[i].isupper():
                for j, letter in enumerate(up_ref):
                    if input_string[i] == letter:
                        encoded_string += up_ref[(j - 1) % 26]
                        break
            elif input_string[i].islower():
                for j, letter in enumerate(low_ref):
                    if input_string[i] == letter:
                        encoded_string += low_ref[(j + 1) % 26]
                        break
    return encoded_string


input_string = input("Enter your message to be decoded: ")
if input_string.isalpha():
    length = len(input_string)
    decode_string = decoder(input_string, length)
    print("Your decoded string is:", decode_string)
else:
    print("Please enter a valid string (letters only)")
