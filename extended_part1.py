#adding AND query
import project
def and_query(key1,key2):
	if project.valid_key(key1) and project.valid_key(key2):
		k1 = project.mock_data_dic[key1]
		k2 = project.mock_data_dic[key2]
		return and_key(k1,k2,"MOCK_DATA.csv")
	else:
		return "No result."

def and_key(k1,k2,filename):
	f = project.file_reader(filename)
	l = []
	for i in k1:
		if i in k2:
			l.append(f[int(i)])
	return l


print (and_query("Inc","Church"))

#adding OR query

def or_query(key1,key2):
	if project.valid_key(key1) or project.valid_key(key2):
		k1 = project.mock_data_dic[key1]
		k2 = project.mock_data_dic[key2]
		return or_key(k1,k2,"MOCK_DATA.csv")
	else:
		return "No result."

def or_key(k1,k2,filename):
	f = project.file_reader(filename)
	l = k1
	l.extend(k2)
	l=set(l)
	return [f[int(i)] for i in l]

a = or_query("Inc", "Church")
