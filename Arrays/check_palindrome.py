def isPalindrome(s):
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False
    
print(isPalindrome("TenEt"))