import math

def ten_to_base(num_in, base_out):  
    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_in = int(num_in)
    power = int(math.log(num_in, base_out))
    retlist = []
    temp_num = num_in
    wring = ''

    while power >= 0:
        place = int(temp_num / (base_out ** power))
        retlist.append(place)
        temp_num -= place * (base_out ** power)
        power -= 1
    for num in retlist:
        wring += char_key[num]
    return wring

def base_to_ten(num_in, base_in):
    num_in = str(num_in)
    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    retlist = []
    for char in num_in:
        retlist.append(char_key.find(char))
    power = len(retlist) - 1
    retcount = 0
    for char in retlist:
        retcount += char * (base_in ** power)
        power -= 1
    return retcount

def base_to_base(num_in, base_in, base_out):
    return ten_to_base(base_to_ten(num_in, base_in), base_out)

if __name__ == "__main__":
    print(base_to_ten('1010', 2))