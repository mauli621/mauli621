class Solution(object):
    def checkString(self, s):
        found_b = False

        for i in range(len(s)):
            if s[i] == 'b':
                found_b = True

            elif s[i] == 'a' and found_b:
                return False

        return True