import inspect


# -----------------------------------Get Char At Index From String-----------------------------------#
def GetCharAtIndexFromString(baseString, charIndex):
    """
    Get a character from string for mentioned index
    :param str: Base string
    :param charIndex: Index within string
    :return: Character at index
    """
    if (charIndex > len(baseString)):
        print("Char index: " + str(charIndex) + " is greater than length: " + str(len(baseString)) + " of base string.")
        return ""
    else:
        charAtIndex = baseString[charIndex]
        return charAtIndex


# char = print(GetCharAtIndexFromString("Sandeep Dhamale", 8))

# -----------------------------------Get String At Index Range From String-----------------------------------#
def GetStringAtIndexRangeFromString(baseString, strStartIndex, strEndIndex):
    """
    Get substring based on provided start index and end index
    :param str: Base string
    :param strStartIndex: Start index
    :param strEndIndex: End index
    :return: Substring from start index to end index
    """
    if (strStartIndex > len(baseString)):
        print("Char start index: " + str(strStartIndex) + " is greater than length: " + str(
            len(baseString)) + " of base string.")
        return ""
    elif (strEndIndex > len(baseString)):
        print("Char end index " + str(strEndIndex) + " is greater than length " + str(
            len(baseString)) + " of base string.")
        return ""
    elif (strStartIndex >= strEndIndex):
        print("Char start index " + str(strStartIndex) + " should be less than end index " + str(strEndIndex) + ".")
        return ""
    else:
        stringAtIndex = baseString[strStartIndex:strEndIndex]
        return stringAtIndex


# char = print(GetStringAtIndexRangeFromString("Sandeep Dhamale", 8, 12))

# -----------------------------------Get Type Of Function-----------------------------------#
def GetTypeOfFunction(functionName):
    """
    Get type of function
    :param functionName: Name of the function
    :return: Type of function
    """
    typeOfFunction = type(functionName)
    return typeOfFunction


# functionType = print(GetTypeOfFunction(GetCharAtIndexFromString("Sandeep Dhamale", 5)))

# -----------------------------------Get Name of variable-----------------------------------#
def retrieve_name(var):
    """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]

# -----------------------------------Swap strings-----------------------------------#
def swap_strings(string1, string2):
    string1, string2 = string2, string1
    return  string1, string2