#!/usr/bin/env python3
import sys


# []
def l(*lst):
    if len(lst) == 1:
        return(lst[0], 0)
    if len(lst) == 2:
        return lst
    else:
        ## LINE 2
        return (lst[0], l(*lst[1:]))


# *
def nock(noun):
    ## LINE 1
    return tar(noun)


# ?
def wut(noun):
    if isinstance(noun, int):
        ## LINE 5
        return 1
    else:
        ## LINE 4
        return 0


# +
def lus(noun):
    if isinstance(noun, int):
        ## LINE 7
        return 1 + noun
    else:
        ## LINE 6
        return noun


# =
def tis(noun):
    if noun[0] == noun[1]:
        ## LINE 8
        return 0
    else:
        ## LINE 9
        return 1


# this has a name in Nock so no need to call it fas
# /
def slot(noun):
    if noun[0] == 1:
        ## LINE 11
        return noun[1]
    elif noun[0] == 2:
        ## LINE 12
        return noun[1][0]
    elif noun[0] == 3:
        ## LINE 13
        return noun[1][1]
    elif noun[0] % 2 == 0:
        ## LINE 14
        return slot((2, slot((noun[0] // 2, noun[1]))))
    elif noun[0] % 2 == 1:
        ## LINE 15
        return slot((3, slot(((noun[0] - 1) // 2, noun[1]))))


def tar(noun):
    if isinstance(noun[1][0], int):
        if noun[1][0] == 0:
            ## LINE 19
            return slot((noun[1][1], noun[0]))
        elif noun[1][0] == 1:
            ## LINE 20
            return noun[1][1]
        elif noun[1][0] == 2:
            ## LINE 21
            return nock((nock((noun[0], noun[1][1][0])), nock((noun[0], noun[1][1][1]))))
        elif noun[1][0] == 3:
            ## LINE 22
            return wut(nock((noun[0], noun[1][1])))
        elif noun[1][0] == 4:
            ## LINE 23
            return lus(nock((noun[0], noun[1][1])))
        elif noun[1][0] == 5:
            ## LINE 24
            return tis(nock((noun[0], noun[1][1])))
        elif noun[1][0] == 6:
            ## LINE 26
            return nock(l(noun[0], 2, (0, 1), 2, l(1, noun[1][1][1][0], noun[1][1][1][1]), (1, 0), 2, l(1, 2, 3), (1, 0), 4, 4, noun[1][1][0]))
        elif noun[1][0] == 7:
            ## LINE 27
            return nock(l(noun[0], 2, noun[1][1][0], 1, noun[1][1][1]))
        elif noun[1][0] == 8:
            ## LINE 28
            return nock(l(noun[0], 7, l(l(7, (0, 1), noun[1][1][0]), 0, 1), noun[1][1][1]))
        elif noun[1][0] == 9:
            ## LINE 29
            return nock(l(noun[0], 7, noun[1][1][1], l(2, (0, 1), (0, noun[1][1][0]))))
        elif noun[1][0] == 10:
            if isinstance(noun[1][1][0], int):
                ## LINE 31
                return nock((noun[0], noun[1][1][1]))
            else:
                ## LINE 30
                return nock(l(noun[0], 8, noun[1][1][0][1], 7, (0, 3), noun[1][1][1][0]))
    else:
        ## LINE 17
        return (nock((noun[0], noun[1][0])), nock((noun[0], noun[1][1])))

'''
  end of interpreter.
  beginning of nock string parser.
'''


# is this string a natural number?
def is_atom(s):
  for c in s:
    if c not in "0123456789":
      return False
  return True


# is this is a cell that starts and ends with "[" and "]"?
# is this an xplicit cell
def is_xcell(s):
  l = len(s)
  bcnt = 0 
  
  if s[0] != "[":
    return False

  for (i, c) in enumerate(s):
    if c == "[":
      bcnt += 1
    if c == "]":
      bcnt -= 1

    if bcnt == 0:
      return i == l - 1 
          

# split on the fist space where bcnt == 0
# aka split after the first noun
def split_cell(s):
  if is_xcell(s):
    s = s[1:-1]

  bcnt = 0 
  for (i, c) in enumerate(s):
    if c == "[":
      bcnt += 1
    if c == "]":
      bcnt -= 1

    if c == " " and bcnt == 0:
      return [s[:i], s[i+1:]]

  return [-1, -1] 


# takes a string with nocks noun syntax
# returns the python list tree for that noun
def parse_noun(s):
  if is_atom(s):
    return int(s)

  [h, t] = split_cell(s)
  return [parse_noun(h), parse_noun(t)]


if __name__ == "__main__":
  noun = sys.argv[1]
  noun = parse_noun(noun)
  res = nock(noun)
  print(res)

