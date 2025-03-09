def int_to_roman(num):
    romen=''
    while num > 0:
        if num >= 1000:
            romen += 'M' * (num//1000)
            num = num % 1000
        elif num>=900:
            romen += 'CM'
            num=num % 900
        elif num >= 500:
            romen += 'D'
            num = num % 500
        elif num >= 400:
            romen += 'CD'
            num = num % 400
        elif num >= 100:
            romen += 'C'* (num//100)
            num = num % 100
        elif num >= 90:
            romen += 'XC'
            num = num % 90
        elif num >= 50:
            romen += 'L'
            num = num % 50
        elif num >= 40:
            romen += 'XL'
            num = num % 40
        elif num >= 10:
            romen += 'X' * (num//10)
            num = num % 10
        elif num >= 9:
            romen += 'IX'
            num = num % 9
        elif num >= 5:
            romen += 'V'
            num = num % 5
        elif num >= 4:
            romen += 'IX'
            num = num % 4
        elif num>=1:
            romen += 'I' * (num//1)
            break
    return romen         
