import json, nltk


def split_into_phrases(words, MaxPhraseLen, MinPhraseLen):
    phrases = []
    current_phrase = ''
    i = 0
    while True:
        if i >= len(words):
            break
        word = words[i]
        if word not in [',', '.', '!', '?', ')', '\n', '#']:
            if current_phrase and (current_phrase[-1] != '('):
                current_phrase += ' '
            current_phrase += word
        else:
            current_phrase += word

        if (len(current_phrase) >= MinPhraseLen) and (len(current_phrase) <= MaxPhraseLen):
            phrases.append(current_phrase)
            current_phrase = ''
            i += 1
            continue

        elif len(current_phrase) >= MaxPhraseLen:
            current_phrase = current_phrase[:-len(word)].strip(' ')
            phrases.append(current_phrase)
            current_phrase = ''

        else:
            i += 1

    if current_phrase:
        phrases.append(current_phrase)

    if phrases and len(phrases[-1]) < MinPhraseLen:
        padding_length = MinPhraseLen - len(phrases[-1])
        phrases[-1] += '#' * padding_length

    return phrases


if __name__ == '__main__':
    # nltk.download('punkt')
    DNAMapFileName = 'DNAMapping.json'
    DNAMapFile = open(DNAMapFileName, 'r')
    Text2DNATable = json.load(DNAMapFile)
    DNAMapFile.close()
    DNACodeLen = 4
    OriginalFileName = 'incorrect-address.txt'
    f = open(OriginalFileName, 'r')
    letters = f.read()
    TotalWords = nltk.word_tokenize(letters)
    DNAMaxLen = 100
    DNAMinLen = 80
    # Divide DNA segments by words
    phrases = split_into_phrases(TotalWords, DNAMaxLen // DNACodeLen, DNAMinLen // DNACodeLen)

    DNATotal = [''] * len(phrases)
    i = 0
    for phrase in phrases:

        DNASegment = ''
        for character in phrase:
            # print(character)
            DNASegment = DNASegment + Text2DNATable[character]
        DNATotal[i] = DNASegment
        i += 1
    del i
    # print('Not in the code book! Skipped')
    # DNATotal[ind] = 'CGTA'

    f.close()

    # print(phrases)
    PhraseFileName = 'incorrect-phrase.json'
    PhraseFile = open(PhraseFileName, 'w')
    json.dump(phrases, PhraseFile)
    PhraseFile.close()

    DNAFileName = OriginalFileName[:-4] + 'DNA.txt'
    DNAZoneFileName = OriginalFileName[:-4] + 'DNAZone.txt'
    DNAFile = open(DNAFileName, 'w')
    DNAZoneFile = open(DNAZoneFileName, 'w')
    for DNASequence in DNATotal:
        DNAFile.write(DNASequence + '\n')
    DNAFile.close()
    zone = 0
    for DNASequence in DNATotal:
        DNAZoneFile.write('Zone' + str(zone) + '\n' + DNASequence + '\n')
        zone += 1
    # DNAFile.close()
    DNAZoneFile.close()
    print('Encoding finished.')
