import json
import math

import nltk


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
    DNAMapFileName = 'DNAMapping.json'
    DNAMapFile = open(DNAMapFileName, 'r')
    Text2DNATable = json.load(DNAMapFile)
    DNAMapFile.close()
    ChangeType = 'all'
    OriginalFileName = ChangeType + '-original.txt'
    f = open(OriginalFileName, 'r')
    originalLetters = f.read()
    original_word_list = nltk.word_tokenize(originalLetters)
    f.close()
    ChangeFileName = 'correct.txt'
    f = open(ChangeFileName, 'r')
    ChangeLetters = f.read()
    change_word_list = nltk.word_tokenize(ChangeLetters)

    f.close()

    PhraseFileName = ChangeType + '-phrase.json'
    PhraseFile = open(PhraseFileName, 'r')
    original_phrases = json.load(PhraseFile)
    PhraseFile.close()
    print(original_phrases)
    print(change_word_list)
    OriginalDNAFileName = OriginalFileName[:-4] + 'DNA.txt'
    f = open(OriginalDNAFileName, 'r')
    OriginalDNATotal = f.readlines()
    f.close()



    temp = dict()
    DNAtemp = dict()
    change_positions = []
    while True:
        change_words_str = input('Please input the changed words.')  # input ### to break
        if change_words_str == '###':
            break
        change_words = eval(change_words_str)
        change_position_str = input('Please input the changed zone.')
        change_position = eval(change_position_str)
        change_positions += change_position
        change_phrases = split_into_phrases(change_words, 30, 20)
        phrase_per_zone = math.ceil(len(change_phrases) / len(change_position))
        start_zone_index = min(change_position)
        for i in range(len(change_phrases)):
            change_phrase = change_phrases[i]
            pos = i // phrase_per_zone
            DNASegment = ''
            for character in change_phrase:
                DNASegment += Text2DNATable[character]
            try:
                DNAtemp[pos + start_zone_index] += DNASegment + '\n'
                temp[pos + start_zone_index] += change_phrase + '\n'

            except:
                DNAtemp[pos + start_zone_index] = DNASegment + '\n'
                temp[pos + start_zone_index] = change_phrase + '\n'

    print(temp)
    print(DNAtemp)
    print(-1)

    ChangeDNAFileName = ChangeType + '-correctDNA.txt'
    DNAFile = open(ChangeDNAFileName, 'w')
    for zone in range(len(original_phrases)):
        DNAFile.write('Zone' + str(zone) + '\n')
        print('Zone' + str(zone) + '\n')
        if zone not in change_positions:
            print(OriginalDNATotal[zone])
            DNAFile.write(OriginalDNATotal[zone])
        else:
            try:
                print(DNAtemp[zone])
                DNAFile.write(DNAtemp[zone])
            except:
                pass

    DNAFile.close()

