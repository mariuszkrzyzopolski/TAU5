def roman(number):
    i = 0
    numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    result = ''
    while number:
        if numerals[i] == numerals[-1]:
            return numerals[i] * number + result
        digit = number % 10
        number = int(number / 10)
        match digit:
            case 1:
                result = numerals[i] + result
            case 2:
                result = numerals[i] * 2 + result
            case 3:
                result = numerals[i] * 3 + result
            case 4:
                result = numerals[i] + numerals[i + 1] + result
            case 5:
                result = numerals[i + 1] + result
            case 6:
                result = numerals[i + 1] + numerals[i] + result
            case 7:
                result = numerals[i + 1] + numerals[i] * 2 + result
            case 8:
                result = numerals[i + 1] + numerals[i] * 3 + result
            case 9:
                result = numerals[i] + numerals[i + 2] + result
        i += 2
    return result
