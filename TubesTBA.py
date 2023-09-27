# A Simple Lexical Analyzer and LL(1) parser to identify valid lexical / token and identify whether a sentence is grammatically correct or not
# By : Kelompok 8 : Aditya Andar Rahim, Irfan Ahmad Asqolani, Muhammad Zalfa Thoriq ~ School of Computing ~ Telkom university

"""
====== Keterangan CFG dan daftar kata yang Valid ======
S → NN VB NN
NN → me | padre | hermanito | abuelo | jugo | churros | novela | zapatos 
VB → beber | cocinero | leer | usar
Simbol non-terminal : S (starting symbol), NN (Noun), VB (Verb) 
Simbol terminal : me, padre, hermanito, abuelo, jugo, churros, novella, zapatos, beber, cocinero, leer, usar
"""

import string 

# Procedure lexical_analyzer
def lexical_analyzer(input_string):
    # initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47',]

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    # spaces before input string
    transition_table[(state, ' ')] = 'q0'

    # update the transition table for the following token: me 
    transition_table[('q0', 'm')] = 'q1'
    transition_table[('q1', 'e')] = 'q46'
    transition_table[('q46', ' ')] = 'q47'
    transition_table[('q46', '#')] = 'accept'
    transition_table[('q47', ' ')] = 'q47'
    transition_table[('q47', '#')] = 'accept'

    # update the transition table for the following token: padre 
    transition_table[('q0', 'p')] = 'q2'
    transition_table[('q2', 'a')] = 'q3'
    transition_table[('q3', 'd')] = 'q4'
    transition_table[('q4', 'r')] = 'q1'
    transition_table[('q1', 'e')] = 'q46'

    # update the transition table for the following token: abuelo 
    transition_table[('q0', 'a')] = 'q5'
    transition_table[('q5', 'b')] = 'q6'
    transition_table[('q6', 'u')] = 'q7'
    transition_table[('q7', 'e')] = 'q8'
    transition_table[('q8', 'l')] = 'q9'
    transition_table[('q9', 'o')] = 'q46'

    # update the transition table for the following token: hermanito 
    transition_table[('q0', 'h')] = 'q10'
    transition_table[('q10', 'e')] = 'q11'
    transition_table[('q11', 'r')] = 'q12'
    transition_table[('q12', 'm')] = 'q13'
    transition_table[('q13', 'a')] = 'q14'
    transition_table[('q14', 'n')] = 'q15'
    transition_table[('q15', 'i')] = 'q16'
    transition_table[('q16', 't')] = 'q9'
    transition_table[('q9', 'o')] = 'q46'

    # update the transition table for the following token: jugo 
    transition_table[('q0', 'j')] = 'q17'
    transition_table[('q17', 'u')] = 'q18'
    transition_table[('q18', 'g')] = 'q9'
    transition_table[('q9', 'o')] = 'q46'

    # update the transition table for the following token: cocinero 
    transition_table[('q0', 'c')] = 'q19'
    transition_table[('q19', 'o')] = 'q20'
    transition_table[('q20', 'c')] = 'q21'
    transition_table[('q21', 'i')] = 'q22'
    transition_table[('q22', 'n')] = 'q23'
    transition_table[('q23', 'e')] = 'q24'
    transition_table[('q24', 'r')] = 'q9'
    transition_table[('q9', 'o')] = 'q46'

    # update the transition table for the following token: churros 
    transition_table[('q0', 'c')] = 'q19'
    transition_table[('q19', 'h')] = 'q25'
    transition_table[('q25', 'u')] = 'q26'
    transition_table[('q26', 'r')] = 'q27'
    transition_table[('q27', 'r')] = 'q28'
    transition_table[('q28', 'o')] = 'q29'
    transition_table[('q29', 's')] = 'q46'

    # update the transition table for the following token: zapatos 
    transition_table[('q0', 'z')] = 'q30'
    transition_table[('q30', 'a')] = 'q31'
    transition_table[('q31', 'p')] = 'q32'
    transition_table[('q32', 'a')] = 'q33'
    transition_table[('q33', 't')] = 'q28'
    transition_table[('q28', 'o')] = 'q29'
    transition_table[('q29', 's')] = 'q46'

    # update the transition table for the following token: leer
    transition_table[('q0', 'l')] = 'q34'
    transition_table[('q34', 'e')] = 'q35'
    transition_table[('q35', 'e')] = 'q36'
    transition_table[('q36', 'r')] = 'q46'

    # update the transition table for the following token: beber
    transition_table[('q0', 'b')] = 'q37'
    transition_table[('q37', 'e')] = 'q38'
    transition_table[('q38', 'b')] = 'q35'
    transition_table[('q35', 'e')] = 'q36'
    transition_table[('q36', 'r')] = 'q46'

    # update the transition table for the following token: usar
    transition_table[('q0', 'u')] = 'q39'
    transition_table[('q39', 's')] = 'q40'
    transition_table[('q40', 'a')] = 'q36'
    transition_table[('q36', 'r')] = 'q46'

    # update the transition table for the following token: novela
    transition_table[('q0', 'n')] = 'q41'
    transition_table[('q41', 'o')] = 'q42'
    transition_table[('q42', 'v')] = 'q43'
    transition_table[('q43', 'e')] = 'q44'
    transition_table[('q44', 'l')] = 'q45'
    transition_table[('q45', 'a')] = 'q46'

    # transition for new token 
    transition_table[('q47', 'm')] = 'q1'
    transition_table[('q47', 'p')] = 'q2'
    transition_table[('q47', 'a')] = 'q5'
    transition_table[('q47', 'h')] = 'q10'
    transition_table[('q47', 'j')] = 'q17'
    transition_table[('q47', 'c')] = 'q19'
    transition_table[('q47', 'z')] = 'q30'
    transition_table[('q47', 'l')] = 'q34'
    transition_table[('q47', 'b')] = 'q37'
    transition_table[('q47', 'u')] = 'q39'
    transition_table[('q47', 'n')] = 'q41'

    # Lexical Analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    print('')
    print('---- Lexical Analyzer ----')
    while state !='accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q46':
            print('current token: ',current_token,', valid')
            current_token = ''
        if state=='error':
            print('error')
            print('')
            break;
        idx_char = idx_char + 1

    #conclusion
    if state=='accept':
        print('semua token diinput: ', sentence, ', valid')
        print('')
        return True
    else:
        return False

# Procedure parser LL(1)
def parser(tokens):
    # symbols definition
    non_terminals = ['S', 'NN', 'VB']
    terminals = ['me', 'padre', 'abuelo', 'hermanito', 'jugo', 'cocinero', 'churros', 'zapatos', 'leer', 'beber', 'usar', 'novela' ]

    # parse table definition
    parse_table = {}

    # class S
    parse_table[('S', 'me')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'padre')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'hermanito')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'abuelo')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'beber')] = ['error']
    parse_table[('S', 'cocinero')] = ['error']
    parse_table[('S', 'leer')] = ['error']
    parse_table[('S', 'usar')] = ['error']
    parse_table[('S', 'jugo')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'churros')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'novela')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'zapatos')] = ['NN', 'VB', 'NN']
    parse_table[('S', 'EOS')] = ['error']

    # class NN
    parse_table[('NN', 'me')] = ['me']
    parse_table[('NN', 'padre')] = ['padre']
    parse_table[('NN', 'hermanito')] = ['hermanito']
    parse_table[('NN', 'abuelo')] = ['abuelo']
    parse_table[('NN', 'beber')] = ['error']
    parse_table[('NN', 'cocinero')] = ['error']
    parse_table[('NN', 'leer')] = ['error']
    parse_table[('NN', 'usar')] = ['error']
    parse_table[('NN', 'jugo')] = ['jugo']
    parse_table[('NN', 'churros')] = ['churros']
    parse_table[('NN', 'novela')] = ['novela']
    parse_table[('NN', 'zapatos')] = ['zapatos']
    parse_table[('NN', 'EOS')] = ['error']

    # class VB
    parse_table[('VB', 'me')] = ['error']
    parse_table[('VB', 'padre')] = ['error']
    parse_table[('VB', 'hermanito')] = ['error']
    parse_table[('VB', 'abuelo')] = ['error']
    parse_table[('VB', 'beber')] = ['beber']
    parse_table[('VB', 'cocinero')] = ['cocinero']
    parse_table[('VB', 'leer')] = ['leer']
    parse_table[('VB', 'usar')] = ['usar']
    parse_table[('VB', 'jugo')] = ['error']
    parse_table[('VB', 'churros')] = ['error']
    parse_table[('VB', 'novela')] = ['error']
    parse_table[('VB', 'zapatos')] = ['error']
    parse_table[('VB', 'EOS')] = ['error']

    # stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]
    print('--------- Parser ---------')
    # parsing process
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        print('top = ',top)
        print('symbol = ',symbol)
        if top in terminals:
            print('top adalah simbol terminal')
            if top==symbol:
                stack.pop()
                idx_token = idx_token + 1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    print('isi stack:',stack)
                    stack.pop()
            else:
                print('error')
                print('')
                break;
        elif top in non_terminals:
            print('top adalah simbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                print('error')
                print('')
                break;
        else: 
            print('error')
            print('')
            break;
        print('isi stack:',stack)
        print('')

    # conclusion
    if symbol == 'EOS' and len(stack)==0:
        return True
    else:
        return False
            

# main program

sentence = input('Kalimat Uji: ')

while sentence != 'quit':

    input_string = sentence.lower()+'#'
    tokens = sentence.lower().split()
    tokens.append('EOS')

    result_lexical = lexical_analyzer(input_string)
    if (result_lexical):
        result_parser = parser(tokens)
        print('Kesimpulan:')
        if (result_parser):
            print("Lexical Analyzer: Valid")
            print("Parser: Valid")
            print('Kalimat Uji:', sentence, ', diterima karena sesuai dengan simbol terminal dan aturan pada grammar')
        else:
            print("Lexical Analyzer: Valid")
            print("Parser: Not Valid")
            print('Error, Kalimat Uji:', sentence, ', tidak diterima karena tidak sesuai dengan aturan pada grammar')
    else:
        print('Kesimpulan:')
        print("Lexical Analyzer: Not Valid")
        print('Error, Kalimat Uji:', sentence, ', tidak diterima karena tidak sesuai dengan simbol terminal yang didefinisikan')
        
    print('')
    sentence = input('Kalimat Uji: ')
