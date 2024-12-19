#!/user/bin/python3

import re
import sys
import os

label_size = 8
comment_col = 30

def format():
    prevblank = False
    with open(sys.argv[1]) as inf:
        for line in inf.readlines():
            line = line[:-1].rstrip()
            if line:
                prevblank = False
                if line[0]=='/' :
                    result = line
                else:
                    m = re.match(r'(\s*)([^,/]*,)?([^/]*/)?(.*)', line)
                    pfx, label, precomment, final = m.groups()
                    #print(m.groups())
                    body = (precomment[:-1].rstrip() if precomment \
                            else final).strip()
                    comment = (final if precomment else '').strip()
                    result = ''
                    if pfx or label:
                        if label:
                            result = (label[:-1].strip() + ',')
                        result = result.ljust(label_size) + body
                    else:
                        s = line.split('/')
                        result, comment = s[0], s[1] if len(s)>1 else ''
                        result.rstrip()
                    if comment:
                        result = result.ljust(comment_col) + \
                            '/ ' + comment.strip()
            else:              # blank line
                result = None if prevblank else line
                prevblank = True
            if result is not None:
                print(result)


format()            
            
