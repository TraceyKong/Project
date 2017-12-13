#inverted index
import csv
import pycountry

def file_reader(filename):
    csv_reader = csv.reader(open(filename))
    return [line for line in csv_reader]

    
def build_inverted_index(filename,keyindex,textindex):
    d = {}
    f = file_reader(filename)
    for line in f:
        document = line[keyindex]
        textstring = line[textindex]
        wordlist = clean_text(textstring).split() 
        for word in wordlist:
            d.setdefault(word,[])
            d[word].append(document)
    return d

def return_values(keyindex):
    if "ID" in keyindex: keyindex.remove("ID")
    l = list(set(map(int,keyindex)))
    l.sort()
    l = [mock_data[k] for k in l]
    return l

def convert_country(data):
    d = return_values([i[0] for i in data])
    for i in d:
        c = pycountry.countries.get(alpha2=i[3])
        i[3] = str(c.name)

def valid_key(key):
    return key in mock_data_dic.keys()

def clean_text(line):
    cleantext = ""
    for letter in line:
        if letter.isalpha():
            cleantext = cleantext + letter
        else:
            cleantext = cleantext + " "
    return cleantext

mock_data = file_reader("MOCK_DATA.csv")
convert_country(mock_data)
mock_data_dic = build_inverted_index('MOCK_DATA.csv',0,4)