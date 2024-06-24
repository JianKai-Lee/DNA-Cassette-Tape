import random
import itertools


def HomopolymerCalculation(DNACode):
    count = 1
    Homopolymer = 1
    for i in range(len(DNACode) - 1):
        if DNACode[i] == DNACode[i + 1]:
            count += 1
        else:
            Homopolymer = max(Homopolymer, count)
            count = 1
    return max(Homopolymer, count)


def GCCalculation(DNACode):
    GCNum = DNACode.count('G') + DNACode.count('C')
    GCContent = (GCNum / len(DNACode))
    return GCContent


def HomopolymerHeadTail(DNACode, MaxHomopolymer):
    bases = ['A', 'T', 'G', 'C']
    homopolymers = [base * MaxHomopolymer for base in bases]
    if (DNACode.startswith(tuple(homopolymers))):
        # or DNACode.endswith(tuple(homopolymers))):
        return False
    else:
        return True


if __name__ == '__main__':
    DNACodeLen = 4
    DNAIterator = itertools.product('ATGC', repeat=DNACodeLen)
    DNACodeBook = []
    MaxHomopolymer = 2
    file = 'DNACode.txt'
    f = open(file, 'w')
    for DNASegment in DNAIterator:
        DNASegmentStr = ''.join(DNASegment)
        if ((GCCalculation(DNASegmentStr) == 0.5) and (HomopolymerCalculation(DNASegmentStr) <= MaxHomopolymer) and
                HomopolymerHeadTail(DNASegmentStr, MaxHomopolymer)):
            DNACodeBook.append(DNASegmentStr)
    for DNACode in DNACodeBook:
        f.write(DNACode + '\n')
        print(DNACode)
    # print(len(DNACodeBook))
    f.close()

