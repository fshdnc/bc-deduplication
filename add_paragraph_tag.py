import os
import sys

def add_par_tag(fileName, in_dir, out_dir):
    in_file = in_dir + fileName
    with open(in_file) as f:
        lineList = f.readlines()

    # tokenization
    tokList = []
    for line in lineList:
        tokList.append(line.split(' '))

    # add <p>, </p> tags
    parList = [['<p>']]
    for lst in tokList:
        parList.append(lst)
        parList.append(['</p>', '<p>'])
    parList = parList[:-1]
    parList = [t for lst in parList for t in lst]

    out_file = out_dir + fileName
    with open(out_file, 'w') as f:
        f.write('\n'.join(parList))

if __name__ == '__main__':
    files = [f for f in os.listdir(sys.argv[1])]
    txt_files = [f for f in files if f.endswith('.txt')]

    for fileName in txt_files:
        add_par_tag(fileName, sys.argv[1], sys.argv[2])
