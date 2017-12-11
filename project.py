#inverted index
import csv

def file_reader(filename):
    csv_reader = csv.reader(open(filename))
    return [line for line in csv_reader]
    
def build_inverted_index(filename,keyindex,textindex):
    d = {}
    f = file_reader(filename)
    for line in f:
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

def return_values(filename,key):
    f = file_reader(filename)
    d = mock_data_dic 
    v = []
    for k in mock_data_dic[key]:
        v.append(f[int(k)])
    return v

def valid_key(key):
    return key in mock_data_dic.keys()

mock_data_dic = build_inverted_index('MOCK_DATA.csv',0,4)
data_search = return_values('MOCK_DATA.csv','Dollar')
