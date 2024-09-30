def temperature_converter(temp,unit):
    if unit =="C":
        temp = (temp * 1.8) + 32
        unit = " F"
    elif unit == "F":
        temp = (temp - 32) / 1.8
        unit = " C"
    temp = int(temp)
    temp = str(temp)
    return (temp + unit)

def reverse(string):
    string = string [::-1]
    return string

def fib(N):
    count = 0
    hold = 0
    num1 = 0
    num2 = 1
    if N == 0:
        return N
    else:
        while count < (N - 1):
            hold = num1 + num2
            num1 = num2
            num2 = hold
            count = count + 1
        return num2



