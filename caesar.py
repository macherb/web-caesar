def alphabet_position(letter):
    ordinal = ord(letter[0])
    if ordinal >= 65 and ordinal <= 90:
        return ordinal - 65
    elif ordinal >= 97 and ordinal <= 122:
        return ordinal - 97
    else:
        return -1

def rotate_character(char, rot):
    result = char
    if char.isalpha():
        result = alphabet_position(char) + rot
        while result >= 26:
            result -= 26
        if char.isupper():
            result += 65
        else:
            result += 97
        result = chr(result)
    return result

def rotate_string(text, rot):
    result = ""
    for i in text:
        result += rotate_character(i, rot)
    return result

def main():
    message = input('Type a message:\n')
    rotate = input('Rotate by:\n')
    print(rotate_string(message, int(rotate)))

if __name__ == "__main__":
    main()