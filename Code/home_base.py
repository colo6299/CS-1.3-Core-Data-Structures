import math

def ten_to_base(num_in, base_out):  
    neg_flag = False
    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # char_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    if num_in < 0:
        num_in = -num_in
        neg_flag = True
    num_in = int(num_in)
    power = int(math.log(num_in, base_out))
    retlist = []
    temp_num = num_in
    wring = ''
    if neg_flag:
        wring += '-'

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
    neg_mult = 1
    retlist = []
    if num_in and num_in[0] == '-':
        num_in = num_in[1:]
        neg_mult = -1
    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # char_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for char in num_in:
        retlist.append(char_key.find(char))
    power = len(retlist) - 1
    retcount = 0
    for char in retlist:
        retcount += char * (base_in ** power)
        power -= 1
    retcount *= neg_mult
    return retcount

def base_to_ten_krunk(num_in, base_in):
    num_in = str(num_in)
    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # char_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    retlist = []
    for char in num_in:
        retlist.append(char_key.find(char))
    retlist = [23, 32, 62, 2, 39, 16, 58]
    power = len(retlist) - 1
    retcount = 0
    for char in retlist:
        retcount += char * (base_in ** power)
        power -= 1
    return retcount

def base_to_base(num_in, base_in, base_out):
    return ten_to_base(base_to_ten(num_in, base_in), base_out)

if __name__ == "__main__":
    #print(base_to_ten('1010', 2))
    char_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    char_key = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ  '
    aretlist = [
        23, 32, 62, 2, 39, 16, 58,
        29, 8, 5, 8, 29, 57, 50,
        54, 29, 31, 53, 40, 53, 15, 
        31, 56, 29, 54, 23, 2, 29, 
        16, 29, 2, 58, 49, 51, 24,
        60, 15, 20, 64, 10, 26, 16, 
        57, 47, 24, 10, 49, 56, 39
    ]
    retlist = [39,16,24,29,15,50,58,16,57,53,2,51,26,56,49,10,49,23,40,29,39,2,8,53,54,58,64,10,24,20,2,29,31,5,62,32,8,29,56,29,15,47,57,60,16,31,54,29,23]
    print()
    for num in retlist:
        print(char_key[num - 1], end='')
    print()