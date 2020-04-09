'''
argv1 directory containing the text files
argv2 name of the file to be written to

Takes in a directory with text files
Outputs a single text file with document boundary
and paragraphs in vert format
'''

import os
import sys

def add_par_tag(fileName, in_dir, out_file):
    in_file = in_dir + fileName
    with open(in_file) as f:
        lineList = f.readlines()

    # tokenization
    tokList = []
    for line in lineList:
        tokList.append(line.split(' '))

    # add <p>, </p> tags
    parList = []
    for lst in tokList:
        parList.append(['<p>'])
        parList.append(lst)
        parList.append(['</p>'])
    parList = [['<doc>']] + parList + [['</doc>']]
    parList = [t for lst in parList for t in lst]

    with open(out_file, 'a') as f:
        f.write('\n'.join(parList))
        f.write('\n')

if __name__ == '__main__':
    files = [f for f in os.listdir(sys.argv[1])]
    txt_files = [f for f in files if f.endswith('.txt')]

    with open(sys.argv[2], 'w') as f:
        f.write('')

    for fileName in txt_files:
        add_par_tag(fileName, sys.argv[1], sys.argv[2])
