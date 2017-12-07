#inverted index
import csv


def file_reader(filename,keyindex,textindex):
    csv_reader =csv.reader(open(filename))
    l = []
    for line in csv_reader:
        document = line[keyindex]
        textstring = line[textindex]
        cleantext = ""
        for letter in textstring:
            if letter.isalpha():
                cleantext = cleantext + letter
            else:
                cleantext = cleantext + " "
        l.append([document,cleantext])
    return l

def build_inverted_index(filename,keyindex,textindex):
    d = {}
    f = file_reader(filename,0,4)
    for word in f:
        wordlist = word[1].split()
        for w in wordlist:
            d.setdefault(w,[])
            d[w].append(word[0])
    return d

def return_values(filename,key):
    f = file_reader(filename,0,4)
    d = mock_data_dic 
    v = []
    for k in mock_data_dic[key]:
        v.append(f[int(k)])
    return v


mock_data_dic = build_inverted_index('MOCK_DATA.csv',0,4)


print(return_values('MOCK_DATA.csv','Allergy'))
