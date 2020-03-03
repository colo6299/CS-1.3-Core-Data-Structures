from hash_browns import Hashbrowns as Hashtable
from recomper import Combinator
from recomper import Permutator
import cProfile
import sys
import json

def dejumbler(jumble, meltionary):
    melty_word = word_melter(jumble)
    valid_list = []

    if melty_word not in meltionary:
        return valid_list

    for valid_word in meltionary[melty_word]:
        if is_letter_list_permutation(valid_word, jumble):
            valid_list.append(valid_word)
    return valid_list

def multi_dejumble(jumble_letters, word_lengths, meltionary):

    retlist = []
    for _ in range(len(word_lengths)):
        retlist.append([])
    _multi_word_dejumbler(list(jumble_letters), word_lengths, [], retlist, meltionary)
    return retlist

# out_list should be a list of empty list of length len(word_lengths) i.e. [2, 6] -> [ [], [] ] ->
#                                                    -> the result is a list of solutions of length [1, 2]
def _multi_word_dejumbler(jumble_letters, word_lengths, cur_words, out_list, d, _ndx=-1):   

    if len(jumble_letters) == 0:
        let_list = list(cur_words)
        longth = len(cur_words)
        #str_comp = ''.join(jumble_letters)
        #let_list.append(str_comp)
        out_list[len(word_lengths) - longth].append(let_list)

    c = Combinator()
    _ndx += 1
    if _ndx == len(word_lengths):
        return
    for combo, compliment in c.combo_compliments(jumble_letters, word_lengths[_ndx]):
        valid_words = dejumbler(combo, d)
        if len(compliment) == 0:
                print(cur_words)
                let_list = list(cur_words)
                longth = len(cur_words)
                str_comp = ''.join(jumble_letters)
                let_list.append(str_comp)
                out_list[len(word_lengths) - longth].append(let_list)

        if len(valid_words) == 0:
            print(cur_words)
            
        for valid_word in valid_words:
            new_words = list(cur_words)
            new_words.append(valid_word)
            _multi_word_dejumbler(compliment, word_lengths, new_words, out_list, d, _ndx)

def dictionary_melter():
    f = open('big_dict.txt')
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
    f = open('big_dict.txt')
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

def is_letter_list_permutation(llist_1, llist_2):
    
    if len(llist_1) != len(llist_2):
        return False

    fraction_l1 = [0] * 27
    fraction_l2 = [0] * 27
    for letter in llist_1:
        fraction_l1[ord(letter) - 97] += 1
    for letter in llist_2:
        fraction_l2[ord(letter) - 97] += 1

    if fraction_l1 == fraction_l2:
        return True
    else:
        return False

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

def jumble_runner(meltionary):
     
    primary_jumbles = [
        ['tefon', '--o-o'],
        ['sokik', 'oo-o-'],
        ['niumem', '----o-'],
        ['siconu', '---oo-']
    ]

    answers = []
    for jumble in primary_jumbles:
        answers.append(dejumbler(jumble[0], meltionary))

    secondary_word_lengths = [6, 2]
    secondary_letters = ''
    for ndx, jumble in enumerate(primary_jumbles):
        for index, letter in enumerate(jumble[1]):
            if letter == 'o':
                secondary_letters += answers[ndx][0][index]

    secondary_answers_list = multi_dejumble(secondary_letters, secondary_word_lengths, meltionary)

    
    print()
    print(answers)
    print()
    print(secondary_answers_list[0])
    print()

    return (answers, secondary_answers_list)

def trash():
    """
    Just waiting for the garbageman
    """
    """
    c = Combinator()
    combos = c.combinations(list(secondary_letters), seondary_jumble[0])
    possible_secondary_answers = []
    for combo in combos:

        
        compliment = c.compliment(combo, list(secondary_letters))
        combo = word_melter(''.join(combo))
        compliment = word_melter(''.join(compliment))

        answer_1 = dejumbler(combo, meltionary)
        answer_2 = dejumbler(compliment, meltionary)

        if len(answer_1) is not 0 and len(answer_2) is not 0:
            possible_secondary_answers.append((answer_1, answer_2))

    probable_secondary_answers = []
    for possible_answer in possible_secondary_answers:
        probable_secondary_answers.append(possible_answer) 
    """

if __name__ == "__main__":

    #cProfile.run('dictionary_melter()')
    d = dictionary_melter_std()
    #meltionary_writer(d)
    #d = meltionary_reader()
    #meltionary_writer(d)
    #cProfile.run('jumble_runner(d)')
    jumble_runner(d)
    #print(dejumbler('short', d))  # sardine

