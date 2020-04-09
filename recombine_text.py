'''
argv1 name of the file in vert
argv2 name of the file to be written to

Takes in a vert file with documents separated by <doc>, </doc>
and paragraphs separated by <p>, </p>
Outputs a single text file with paragraphs recombined.
'''

import os
import sys


def parse(in_file, out_file):
    cache_p = [] # for lines that are before <doc>
    with open(in_file) as f:
        #count = 0
        while True:
            #count += 1
            #if count%10000==0:
            #    print(count)
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if line == '<doc>':
                #print('<doc>: %s' % count)
                cache_doc = []
            elif line == '</doc>':
                #print('</doc>: %s' % count)
                write_doc(cache_doc, out_file)
            elif line == '<p>':
                cache_p = []
            elif line == '</p>':
                cache_doc.append(' '.join(cache_p))
            else:
                cache_p.append(line)

def write_doc(cache_doc, out_file):
    with open(out_file, 'a+') as f:
        f.write('\n'.join(cache_doc))

if __name__ == '__main__':
    try:
        os. remove(sys.argv[2])
    except FileNotFoundError:
        pass
    #with open(sys.argv[2], 'w') as f:
    #    f.write('')

    parse(sys.argv[1], sys.argv[2])
