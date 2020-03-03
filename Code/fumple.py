from hash_browns import Hashbrowns as Hashtable
import cProfile
import sys
import json

def dejumbler(jumble, meltionary):
    melty_word = word_melter(jumble)
    valid_list = []
    for valid_word in meltionary.get(melty_word):
        if len(valid_word) == len(jumble):
            valid_list.append(valid_word)
    return valid_list

def dictionary_melter():
    f = open('/usr/share/dict/words')
    table = Hashtable()

    index = -1
    while True:
        index += 1
        word = f.readline()
        word = word.strip().lower()
        if word is '':
            f.close()
            return table
        melty = word_melter(word)
        if melty in table:
            table.get(melty).append(word)
        else:
            table.set(melty, [word])

def dictionary_melter_std():
    """
    I know using the pythomn dict is kind of cheating, but I've 
    had enough of serialization ever since I got into Unity
    """
    f = open('/usr/share/dict/words')
    table = {}

    index = -1
    while True:
        index += 1
        word = f.readline()
        word = word.strip().lower()
        if word is '':
            f.close()
            return table
        melty = word_melter(word)
        if melty in table:
            table[melty].append(word)
        else:
            table[melty] = [word]

def word_melter(word):
    letter_array = [None] * 27  # 27 is dash (-)
    for letter in word:
        if letter == '-':
            letter_array[26] = True
        else:
            letter_array[ord(letter) - 97] = True
    retstring = ''
    for index, letter in enumerate(letter_array):
        if letter is True:
            retstring += chr(index + 97)
    return retstring

def meltionary_writer(meltionary):
    dd = json.dumps(meltionary)
    f = open("meltionary.json","w")
    f.write(dd)
    f.close()

def meltionary_reader():
    f = open("meltionary.json","r")
    ds = json.load(f)
    f.close()
    return ds

def jumble_runner():
     
    primary_jumbles = [
        ['tefon', '--o-o'],
        ['sokik', 'oo-o-'],
        ['niumem', '----o-'],
        ['siconu', '---oo-']
    ]
    seondary_jumble = [2, 6]

    d = meltionary_reader()
    answers = []
    for jumble in primary_jumbles:
        answers.append(dejumbler(jumble[0], d))
    return answers

if __name__ == "__main__":
    #cProfile.run('dictionary_melter()')
    #d = dictionary_melter_std()
    #meltionary_writer(d)
    cProfile.run('jumble_runner()')
    #print(jumble_runner())
    #print(dejumbler('short', d))  # sardine

