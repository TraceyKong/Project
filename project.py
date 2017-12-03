#inverted index
import cvs
def build_inverted_index(filename,keyindex,textindex):
    csv_reader =csv.reader(open(filename))
    d={}
    for line in csv_reader:
        document = line[keyindex]
        textstring = line[textindex]
        cleantext = ""
        for letter in textstring:
            if letter.isalpha():
                cleantext = cleantext + letter
            else:
                cleantext = cleantext + " "
        wordlist = cleantext.split()
        for word in wordlist:
            d.setdefault(word,[])
            d[word].append(document)
    return d