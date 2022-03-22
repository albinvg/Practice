## Given a string s, find the length of the longest substring without repeating characters.

str_s = 'abcabcdbd'

def fn_Largest_substring(str_s):
  start = 0
  max_len = 0
  str_sub = ""
  output_str = ""

  for i in range(len(str_s)):
      while str_s[i] in str_sub:
          start += 1
          str_sub = str_s[start:i]
          #print(str_sub)

      str_sub = str_s[start:i+1]

      length = len(str_sub)
      if max_len != max(length, max_len):
          max_len = max(length, max_len)
          output_str = str_sub
      #print (i, length, str_sub)
  return (max_len , output_str)

## print the length of largest susbstring and the corresponding substring
print (fn_Largest_substring(str_s))
