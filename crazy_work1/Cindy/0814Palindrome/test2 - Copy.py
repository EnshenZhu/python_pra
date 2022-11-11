def isPalindrome_1(s, indent):
    """Return True if s is a palindrome and False otherwise"""
    print(indent, "isPalindrome called with", s)
    if len(s) <= 1:
        print(indent, "About to return True from base case")
        return True
    else:
        ans = (s[0] == s[-1]
               and
               isPalindrome_1(s[1:-1], indent + indent)
               )
        print(indent, "About to return", ans)
        return ans


print(isPalindrome_1('abcdeba', ' '))