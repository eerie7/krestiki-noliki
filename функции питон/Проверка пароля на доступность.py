def isvalid_password(password):
    upper,lower,digit=False,False,False
    if len(password)>=8:
        for elem in password:
            if elem.isupper():
                upper = True
            elif elem.isdigit():
                digit = True
            elif elem.islower():
                lower = True
        if upper == False:
            print('Пароль должен содержать минимум 1 заглавную букву')
            return
        elif lower == False:
            print('Пароль должен содержать минимум 1 прописную букву')
            return
        elif digit == False:
            print('Пароль должен содержать минимум 1 цифру')
            return
    else:
        print('Пароль должен содержать не меньше 8 символов')
    if (upper, lower, digit) == (True,True,True):
        print('Пароль подходит')
        return True