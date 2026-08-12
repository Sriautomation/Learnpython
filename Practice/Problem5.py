# Reverse a string with while loop

def reverse_string(s):
    reversed = ""
    index = len(s) - 1

    while index >= 0:
        reversed += s[index]
        index -= 1
    return reversed

str = "kalvi"
print(reverse_string(str))
 