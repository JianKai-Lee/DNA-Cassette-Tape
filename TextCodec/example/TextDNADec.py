import json

if __name__ == '__main__':
    DNAMapFileName = 'DNAMappingReverse.json'
    DNAMapFile = open(DNAMapFileName, 'r')
    DNA2TextTable = json.load(DNAMapFile)
    DNAMapFile.close()
    DNAFileName = 'correct-addressDNA.txt'
    DNAFile = open(DNAFileName, 'r')
    text = []
    UpperFlag = False
    DigitFlag = False
    PuncFlag = False
    DNADict = dict()
    first_phrase_flag = True
    while True:
        DNASequence = DNAFile.readline().strip('\n')
        first_character_flag = True
        # print(DNASequence)
        if DNASequence == '':
            break
        elif 'Zone' in DNASequence:
            continue
        else:
            for i in range(len(DNASequence) // 4):
                DNACode = DNASequence[i * 4: (i + 1) * 4]
                if DNACode == 'CTAG':
                    break
                character = DNA2TextTable[DNACode]
                if (not first_phrase_flag) and first_character_flag and (
                        character not in [',', '.', '!', '?', ')', '\n', '#']):
                    text.append(' ')
                text.append(character)
                first_character_flag = False
        first_phrase_flag = False
    text = ''.join(text).replace('#', '')
    print(text)
    DNAFile.close()
    DecFileName = DNAFileName[:-4] + '-dec.txt'
    DecFile = open(DecFileName, 'w')
    DecFile.write(text)
    DecFile.close()


    # TextFileName = DNAZoneFileName[:-7] + 'Decode.txt'
    # TextFile = open(TextFileName, 'w')
    # TextFile.write(sorted_values_str)
    # TextFile.close()
