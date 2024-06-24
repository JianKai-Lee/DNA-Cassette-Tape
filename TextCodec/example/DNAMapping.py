import json

if __name__ == '__main__':
    DNACodeFileName = 'DNACode.txt'
    DNACodeFile = open(DNACodeFileName, 'r')
    DNACodes = DNACodeFile.readlines()
    DNACodebook = [DNACode.strip('\n') for DNACode in DNACodes]
    characters = ('abcdefghijklmnopqrstuvwxyz''ABCDEFGHIJKLMNOPQRSTUVWXYZ''0123456789'' ''\n'',''.''!''?''#''('')')
    mapping = dict(zip(characters, DNACodebook))
    DNAMapFileName = 'DNAMapping.json'
    DNAMapFile = open(DNAMapFileName, 'w')
    for text, DNACode in mapping.items():
        print(f"{text} -> {DNACode}")
    json.dump(mapping, DNAMapFile)
    DNAMapFile.close()
    reverse_mapping = dict(zip(DNACodebook, characters))
    DNAMapRFileName = 'DNAMappingReverse.json'
    DNAMapRFile = open(DNAMapRFileName, 'w')
    for  DNACode,text in reverse_mapping.items():
        print(f"{DNACode} -> {text}")
    json.dump(reverse_mapping, DNAMapRFile)
    DNAMapRFile.close()