def checkRegex(s, p):
  if (len(p) == 0):
    return (len(s) == 0)

  if (len(p) == 1) or (p[1] != '*'):
    return (len(s) > 0) and ((p[0] == '.') or (s[0] == p[0])) and checkRegex(s[1:], p[1:])

  new_s = s
  while (len(new_s) > 0) and ((new_s[0] == p[0]) or (p[0] == '.')):
    new_s = new_s[1:]
    if (checkRegex(new_s, p[2:])):
      return True
    return checkRegex(s, p[2:])

  class Solution(object):
    def isMatch(self, s, p):
      """
      :type s: str
      :type p: str
      :rtype: bool
      """
      return checkRegex(s, p)
