def isPalindrome(str):
    if str.strip().lower() == str.strip().lower()[::-1]:
        return True
    else:
        return False

print(isPalindrome("Test"))
print(isPalindrome("Hanah"))
print(isPalindrome("racecar"))