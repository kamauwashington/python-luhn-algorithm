import re


def luhn(input : str) -> bool :
    if input is None : 
        return False

    #  keep it clean and pure to avoid failure, strip all non numeric characters from the input    
    workingInput : str = re.sub(r"[^\d]","",input)

    #  ensure that there are at least two digits
    if len(workingInput) < 2 :
        return False

    #  define known math for the luhn algorithm via array : if doubling a number results in a two digit number,
    #  add the digits of the product to get a single digit number. This is simple pre math, for a lookup style 
    #  solution, vs inline math. for x being any number 0 through 9, x >= 5 then (x * 2) - 9 else x * 2
    knownLuhnValues : list[int] = [0,2,4,6,8,1,3,5,7,9]

    #  this is to be the summed result of the luhn math pre mod test
    completedSum : int = 0

    #  convert the input string into a character array, converting the characters into digits
    inputAsNums = [int(i) for i in list(workingInput)]

    #  loop through the inputs in reverse as per the luhn spec
    for index,num in enumerate(reversed(inputAsNums)) :
        #  apply the known luhn value using the number as the index if a second digit
        completedSum += knownLuhnValues[num] if index % 2 == 1 else num
       
    #  the completedSum should be divisible by 10
    return completedSum % 10 == 0

