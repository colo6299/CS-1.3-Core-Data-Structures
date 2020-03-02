import math

def ten_to_base(num_in, base_out):  

    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.' # decimal 62

    num_in = float(num_in)
    power = int(math.log(num_in, base_out))
    retlist = []
    temp_num = num_in
    wring = ''

    while power >= -10:
        place = int(temp_num / (base_out ** power))
        retlist.append(place)
        temp_num -= place * (base_out ** power)
        if power == 0:
            retlist.append(62)
        power -= 1
    for num in retlist:
        wring += char_key[num]
    return wring


def base_to_ten(num_in, base_in):
    num_in = str(num_in)
    retlist = []
    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.'
    for char in num_in:
        retlist.append(char_key.find(char))
    power = num_in.find('.')
    if power == -1:
        power = len(num_in) -1
    retcount = 0
    for char in retlist:
        if char is not 62:          
            retcount += char * (base_in ** power)
            power -= 1
    return retcount

def base_to_base(num_in, base_in, base_out):
    return ten_to_base(base_to_ten(num_in, base_in), base_out)

if __name__ == "__main__":
    print(ten_to_base(101.52, 16))
    print(base_to_ten(101.1101, 2))
    print(base_to_base(101.11, 2, 13))