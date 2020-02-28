import string 

def clean_string(text):
    text = str.upper(text)
    text = text.translate(str.maketrans('', '', string.whitespace))
    return text.translate(str.maketrans('', '', string.punctuation))

def is_palindrome_iterative(text_in):
    text = clean_string(text_in)
    if len(text) < 2:
        return True
    for i in range(len(text)//2):
        if text[i] is not text[len(text) - 1 - i]:
            return False
    return True

def is_palindrome_iterative_old(text_in):
    text = clean_string(text_in)
    print(text)
    print(len(text))

    upper_index = 0
    lower_index = 0

    if len(text) % 2 == 0:
        upper_index = len(text) / 2
        lower_index = lower_index - 1
    else:
        upper_index = int(len(text) / 2)
        lower_index = upper_index

    while lower_index >= 0:
        print(upper_index, end=' is ')
        print(text[upper_index])
        print(lower_index, end=' is ')
        print(text[lower_index])
        if text[lower_index] != text[upper_index]:
            print('FAILED! ' + text)
            return False
        lower_index -= 1
        upper_index += 1
    return True