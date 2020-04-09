'''
argv1 name of the file in vert
argv2 name of the directory the books to be written into

Takes in a vert file with documents separated by <doc>, </doc>
and paragraphs separated by <p>, </p>
Outputs to books with paragraphs recombined.
'''

import os
import sys


def parse(in_file, out_dir):
    cache_p = [] # for lines that are before <doc>
    with open(in_file) as f:
        count = 0
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
                write_book(cache_doc, out_dir, count)
                count += 1
            elif line == '<p>':
                cache_p = []
            elif line == '</p>':
                cache_doc.append(' '.join(cache_p))
            else:
                cache_p.append(line)

def write_book(cache_doc, out_dir, count):
    out_file = out_dir + "book_" + str(count)
    with open(out_file, 'w') as f:
        f.write('\n'.join(cache_doc))

if __name__ == '__main__':
    assert os.listdir(sys.argv[2]) == [], "Output directory already has file(s)"

    #with open(sys.argv[2], 'w') as f:
    #    f.write('')

    parse(sys.argv[1], sys.argv[2])
