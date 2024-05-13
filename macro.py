def Macro(MacroName,Macro):
    if MacroName == '':
        print('MacroName cannot be blank')
        exit()
    if Macro == '':
        print('Macro cannot be blank')
        exit()

    string = Macro
    macro = '        '+MacroName+': '+MacroName+' {\r            compatible = "zmk,behavior-macro";\r            #binding-cells = <0>;\r            bindings\r                = '

    previous_letter_capital = False
    firstrun = True

    for i in string:
        if previous_letter_capital is True:
            if i.isupper():
                macro += ' &kp '+i
                previous_letter_capital = True
            else:
                previous_letter_capital = False
                macro += '>\r                , <&macro_release &kp LSHFT>\r                , <&kp '
                if i.islower():
                    macro += i
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
    macro += '>\r                ;\r        }; \r//keybinding is <&'+MacroName+'>'

        
    f = open(MacroName+"_macro.txt", "w")
    f.write(macro)
    f.close()

M = input('Macroname :')
N = input('Macro :')
Macro(M,N)