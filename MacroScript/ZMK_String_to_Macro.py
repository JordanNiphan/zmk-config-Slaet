"""

Python program to convert a single line string into ZMK macro format.

Outputs a txt file: (MacroName)_macro.txt
    Duplicate filenames are overwritten.

Optionally combines all *._macro.txt files, in the current directory, into Combined_Macro_File.txt

"""

import os

def MacroFilesCombine():
    MacroFiles = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if 'Combined_Macro_File.txt' in f:
            print('Combined file detected and will be overwritten')
            cont = input('Continue? (Y/n) :')
            if cont.upper() != 'Y':
                print('Stopping')
                exit()

    for f in files:
        if '_macro.txt' in f:
            MacroFiles.append(f)
    if len(MacroFiles) > 0:
        print('Combining')
        print(MacroFiles)
        print(os.getcwd()+'\\Combined_Macro_File.txt')
        f = open('Combined_Macro_File.txt', 'w')
        for l in MacroFiles:
            x = open(l,'r')
            f.write(x.read())
            x.close()
        f.close()
def Macro(MacroName,Macro):

    MacroFileName = MacroName+'_macro.txt'
    string = Macro
    macro =  '        //keybinding is <&'+MacroName+'>\r        '+MacroName+': '+MacroName+' {\r            compatible = "zmk,behavior-macro";\r            #binding-cells = <0>;\r            bindings\r                = '

    previous_letter_capital = False
    firstrun = True

    for i in string:
        if previous_letter_capital is True:
            if i.isupper():
                macro += ' &kp '+i
                previous_letter_capital = True
            else:
                previous_letter_capital = False
                macro += '>\r                , <&macro_release &kp LSHFT>\r                , <&macro_tap &kp '
                if i.islower():
                    macro += i.upper()
                elif i == ' ':
                    macro += 'SPACE'
                elif i == '!':
                    macro += 'EXCL'
                elif i == '@':
                    macro += 'AT'
                elif i == '#':
                    macro += 'HASH'
                elif i == '$':
                    macro += 'DLLR'
                elif i == '%':
                    macro += 'PRCNT'
                elif i == '^':
                    macro += 'CARET'
                elif i == '&':
                    macro += 'AMPS'
                elif i == '*':
                    macro += 'STAR'
                elif i == '(':
                    macro += 'LPAR'
                elif i == ')':
                    macro += 'RPAR'
                elif i == '=':
                    macro += 'EQUAL'
                elif i == '+':
                    macro += 'PLUS'
                elif i == '-':
                    macro += 'MINUS'
                elif i == '_':
                    macro += 'UNDER'
                elif i == '/':
                    macro += 'FSLH'
                elif i == '?':
                    macro += 'QMARK'
                elif i == "\\":
                    macro += 'BSLH'
                elif i == '|':
                    macro += 'PIPE'
                elif i == ';':
                    macro += 'SEMI'
                elif i == ':':
                    macro += 'COLON'
                elif i == "'":
                    macro += 'SQT'
                elif i == '"':
                    macro += 'DQT'
                elif i == ',':
                    macro += 'COMMA'
                elif i == '<':
                    macro += 'LT'
                elif i == '.':
                    macro += 'DOT'
                elif i == '>':
                    macro += 'GT'
                elif i == '{':
                    macro += 'LBKT'
                elif i == '}':
                    macro += 'RBKT'
                elif i == '`':
                    macro += 'GRAVE'
                elif i == '~':
                    macro += 'TILDE'
        else:
            if firstrun == True:
                if i.isupper():
                    macro += '<&macro_press &kp LSHFT> '+ '\r                , <&macro_tap &kp '+i
                    previous_letter_capital = True
                    firstrun = False
                else:
                    macro += '<&macro_tap &kp '+i.upper()
                    previous_letter_capital = False
                    firstrun = False
            elif i == ' ':
                macro += ' &kp SPACE'
            elif i == '!':
                macro += ' &kp EXCL'
            elif i == '@':
                macro += ' &kp AT'
            elif i == '#':
                macro += ' &kp HASH'
            elif i == '$':
                macro += ' &kp DLLR'
            elif i == '%':
                macro += ' &kp PRCNT'
            elif i == '^':
                macro += ' &kp CARET'
            elif i == '&':
                macro += ' &kp AMPS'
            elif i == '*':
                macro += ' &kp STAR'
            elif i == '(':
                macro += ' &kp LPAR'
            elif i == ')':
                macro += ' &kp RPAR'
            elif i == '=':
                macro += ' &kp EQUAL'
            elif i == '+':
                macro += ' &kp PLUS'
            elif i == '-':
                macro += ' &kp MINUS'
            elif i == '_':
                macro += ' &kp UNDER'
            elif i == '/':
                macro += ' &kp FSLH'
            elif i == '?':
                macro += ' &kp QMARK'
            elif i == '\\':
                macro += ' &kp BSLH'
            elif i == '|':
                macro += ' &kp PIPE'
            elif i == ';':
                macro += ' &kp SEMI'
            elif i == ':':
                macro += ' &kp COLON'
            elif i == "'":
                macro += ' &kp SQT'
            elif i == '"':
                macro += ' &kp DQT'
            elif i == ',':
                macro += ' &kp COMMA'
            elif i == '<':
                macro += ' &kp LT'
            elif i == '.':
                macro += ' &kp DOT'
            elif i == '>':
                macro += ' &kp GT'
            elif i == '{':
                macro += ' &kp LBKT'
            elif i == '}':
                macro += ' &kp RBKT'
            elif i == '`':
                macro += ' &kp GRAVE'
            elif i == '~':
                macro += ' &kp TILDE'
            elif i.isupper() == True:
                macro += '>\r                , <&macro_press &kp LSHFT> '+'\r                , <&macro_tap &kp '+i
                previous_letter_capital = True
            else:
                macro += ' &kp '+i.upper()
                previous_letter_capital = False
    if string[-1].isupper() == True:
        macro += '>\r                , <&macro_release &kp LSHFT'
    macro += '>\r                ;\r            };\r'
    
    print('Creating a file for string:')
    print(string)
    print('Filename: '+MacroName+'_macro.txt')
    f = open(MacroName+'_macro.txt', 'w')
    f.write(macro)
    f.close()

    return(MacroFileName)
def StringToMacro():
    files = []
    special_characters = '!@#$%^&*()-+?=,<>/\\\"\''
    work_counter = 0
    annoy_counter = 0
    while True:
        if work_counter == 0:
            print('Ready to work.')
            work_counter += 1
        elif work_counter == 1:
            print('Be happy to.')
            work_counter += 1
        elif work_counter == 2:
            print('Work, work.')
            work_counter += 1
        elif work_counter == 3:
            print('Okie dokie.')
            work_counter += 1
        elif work_counter == 4:
            print('I can do that.')
            work_counter = 0
            
        M = input('Macroname :')

        if any(c in special_characters for c in M):
            print('MacroName cannot contain special characters.')
            if work_counter != 0:
                work_counter -= 1
            continue
        if M == '':
            print('MacroName cannot be blank')
            if work_counter != 0:
                work_counter -= 1
            continue
        if ' ' in M:
            print("MacroName won't work with spaces")
            NewM = ''
            for i in M:
                if i == ' ':
                    NewM += '_'
                else:
                    NewM += i
            M = NewM
            print("Changing MacroName to: "+M)

        N = input('Macro :')
        if N == '':
            print('Macro cannot be blank')
            if work_counter != 0:
                work_counter -= 1
            continue

        
        files.append(Macro(M,N))
        another = input('Create another Macro? (Y/n):')
        if another.upper() == 'Y':
            pass
        elif another.upper() == 'N':
            print('OK!')
            break
        else:
            while True:
                if another.upper() == 'Y':
                    break
                elif another.upper() == 'N':
                    print('FINE!')
                    break
                if annoy_counter == 0:
                    another = input("Whaaat? ... input Y or N ... :")
                    annoy_counter += 1
                elif annoy_counter == 1:
                    another = input("Me busy. Leave me alone!! ... input Y or N ... :")
                    annoy_counter += 1
                elif annoy_counter == 2:
                    another = input("No time for play. ... input Y or N ... :")
                    annoy_counter += 1
                elif annoy_counter == 3:
                    another = input("Me not that kind of orc! ... input Y or N ... :")
                    annoy_counter += 1
                elif annoy_counter == 4:
                    print("Kill 'em! ...progam exit...")
                    exit()

if __name__ == '__main__':
    
    StringToMacro()
    print('Current Directory: '+os.getcwd())
    combine = input('Create Combined Macros File of current Directory? (Y/n) :')
    
    if combine.upper() != 'Y':
        exit()
    
    else:
        MacroFilesCombine()