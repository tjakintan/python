class Solution(object):

    def intToRoman(self, num):

        def setNumbers(number):
            if number == 1:
                return 'I'
            elif number == 5:
                return 'V'
            elif number == 10:
                return 'X'
            elif number == 50:
                return 'L'
            elif number == 100:
                return 'C'
            elif number == 500:
                return 'D'
            elif number == 1000:
                return 'M'
            else:
                return None

        # num = int(input('num : '))
        max = 3999

        if 1 <= num <= max:
            l = []
            final = []

            thousands = num // 1000
            hundreds = (num // 100) % 10
            tens = (num // 10) % 10
            units = num % 10

            a = str(thousands) + '000'
            b = str(hundreds) + '00'
            c = str(tens) + '0'
            d = str(units)

            l.append(int(a))
            l.append(int(b))
            l.append(int(c))
            l.append(int(d))

            for digits in l:
                if setNumbers(digits) is None:

                    # Thousands
                    if digits // 1000:
                        if digits < 4000:
                            count = 0
                            while digits != 1000:
                                digits = digits - 1000
                                count += 1

                            final.append(setNumbers(1000))

                            for i in range(count): final.append(setNumbers(1000))

                    # Hundredth
                    elif (digits // 100) % 10:

                        if digits < 400:
                            count = 0
                            while digits != 100:
                                digits = digits - 100
                                count += 1

                            final.append(setNumbers(100))

                            for i in range(count): final.append(setNumbers(100))

                        elif 500 < digits < 900:
                            count = 0
                            while digits != 500:
                                digits = digits - 100
                                count += 1

                            final.append(setNumbers(500))

                            for i in range(count): final.append(setNumbers(100))

                        elif digits == 900:
                            final.append('C')
                            final.append('M')

                        elif digits == 400:
                            final.append('C')
                            final.append('D')


                    # Tenth
                    elif (digits // 10) % 10:

                        if digits < 40:
                            count = 0
                            while digits != 10:
                                digits = digits - 10
                                count += 1

                            final.append(setNumbers(10))

                            for i in range(count): final.append(setNumbers(10))

                        elif 50 < digits < 90:
                            count = 0
                            while digits != 50:
                                digits = digits - 10
                                count += 1

                            final.append(setNumbers(50))

                            for i in range(count): final.append(setNumbers(10))

                        elif digits == 90:
                            final.append('X')
                            final.append('C')

                        elif digits == 40:
                            final.append('X')
                            final.append('L')


                    # Unit
                    elif digits % 10:

                        if digits < 4:
                            count = 0
                            while digits != 1:
                                digits = digits - 1
                                count += 1

                            final.append(setNumbers(1))

                            for i in range(count): final.append(setNumbers(1))

                        elif 5 < digits < 9:
                            count = 0
                            while digits != 5:
                                digits = digits - 1
                                count += 1

                            final.append(setNumbers(5))

                            for i in range(count): final.append(setNumbers(1))

                        elif digits == 9:
                            final.append('I')
                            final.append('X')

                        elif digits == 4:
                            final.append('I')
                            final.append('V')



                else:
                    final.append(setNumbers(digits))

            val = ''.join(final)
            print(val)

        else:
            print('invalid')


def setNumbers(number):
    if number == 1:
        return 'I'
    elif number == 5:
        return 'V'
    elif number == 10:
        return 'X'
    elif number == 50:
        return 'L'
    elif number == 100:
        return 'C'
    elif number == 500:
        return 'D'
    elif number == 1000:
        return 'M'
    else:
        return None


num = int(input('num : '))
max = 3999

if 1 <= num <= max:
    # lst = [int(i) for i in str(num)]
    l = []
    final = []

    thousands = num // 1000
    hundreds = (num // 100) % 10
    tens = (num // 10) % 10
    units = num % 10

    a = str(thousands) + '000'
    b = str(hundreds) + '00'
    c = str(tens) + '0'
    d = str(units)

    l.append(int(a))
    l.append(int(b))
    l.append(int(c))
    l.append(int(d))

    for digits in l:
        if setNumbers(digits) is None:

            # Thousands
            if digits // 1000:
                if digits < 4000:
                    count = 0
                    while digits != 1000:
                        digits = digits - 1000
                        count += 1

                    final.append(setNumbers(1000))

                    for i in range(count): final.append(setNumbers(1000))

            # Hundredth
            elif (digits // 100) % 10:

                if digits < 400:
                    count = 0
                    while digits != 100:
                        digits = digits - 100
                        count += 1

                    final.append(setNumbers(100))

                    for i in range(count): final.append(setNumbers(100))

                elif 500 < digits < 900:
                    count = 0
                    while digits != 500:
                        digits = digits - 100
                        count += 1

                    final.append(setNumbers(500))

                    for i in range(count): final.append(setNumbers(100))

                elif digits == 900:
                    final.append('C')
                    final.append('M')

                elif digits == 400:
                    final.append('C')
                    final.append('D')


            # Tenth
            elif (digits // 10) % 10:

                if digits < 40:
                    count = 0
                    while digits != 10:
                        digits = digits - 10
                        count += 1

                    final.append(setNumbers(10))

                    for i in range(count): final.append(setNumbers(10))

                elif 50 < digits < 90:
                    count = 0
                    while digits != 50:
                        digits = digits - 10
                        count += 1

                    final.append(setNumbers(50))

                    for i in range(count): final.append(setNumbers(10))

                elif digits == 90:
                    final.append('X')
                    final.append('C')

                elif digits == 40:
                    final.append('X')
                    final.append('L')


            # Unit
            elif digits % 10:

                if digits < 4:
                    count = 0
                    while digits != 1:
                        digits = digits - 1
                        count += 1

                    final.append(setNumbers(1))

                    for i in range(count): final.append(setNumbers(1))

                elif 5 < digits < 9:
                    count = 0
                    while digits != 5:
                        digits = digits - 1
                        count += 1

                    final.append(setNumbers(5))

                    for i in range(count): final.append(setNumbers(1))

                elif digits == 9:
                    final.append('I')
                    final.append('X')

                elif digits == 4:
                    final.append('I')
                    final.append('V')



        else:
            final.append(setNumbers(digits))

    val = ''.join(final)
    print(val)

else:
    print('invalid')
