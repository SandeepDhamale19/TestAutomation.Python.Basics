from Custom_Functions import StringsHelpers

temp_string = "Sandeep Dhamale"

# Test function for StringsHelpers.GetCharAtIndexFromString
# help(StringsHelpers.GetCharAtIndexFromString)
print("\n1. Test function for StringsHelpers.GetCharAtIndexFromString")
get_char_index = StringsHelpers.GetCharAtIndexFromString(temp_string, 4)
print("\tCharacter at index 4: '" + get_char_index + "' in string " + temp_string)
get_char_index = StringsHelpers.GetCharAtIndexFromString(temp_string, 24)
print("\tCharacter at index 4: '" + get_char_index + "' in string " + temp_string)

# Test function for StringsHelpers.GetStringAtIndexRangeFromString
print("\n2. Test function for StringsHelpers.GetStringAtIndexRangeFromString")
get_substring = StringsHelpers.GetStringAtIndexRangeFromString(temp_string, 5, 9)
print("\tSubstring at start index 5 and end index 9 '" + get_substring + "' in string " + temp_string)
get_substring = StringsHelpers.GetStringAtIndexRangeFromString(temp_string, 24, 9)
print(get_substring)
get_substring = StringsHelpers.GetStringAtIndexRangeFromString(temp_string, 5, 24)
print(get_substring)
get_substring = StringsHelpers.GetStringAtIndexRangeFromString(temp_string, 9, 5)
print(get_substring)
get_substring = StringsHelpers.GetStringAtIndexRangeFromString(temp_string, 5, 5)
print(get_substring)