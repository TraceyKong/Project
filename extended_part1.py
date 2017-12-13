#adding AND query
import project

def and_query(key1,key2):
	if project.valid_key(key1) and project.valid_key(key2):
		k1 = project.mock_data_dic[key1]
		k2 = project.mock_data_dic[key2]
		return project.return_values(and_key(k1,k2))
	else: return None

def and_key(k1,k2):
	return [i for i in k1 if i in k2]

#adding OR query

def or_query(key1,key2):
	if project.valid_key(key1) or project.valid_key(key2):
		k1 = project.mock_data_dic[key1]
		k2 = project.mock_data_dic[key2]
		return project.return_values(or_key(k1,k2))
	else: return None

def or_key(k1,k2):
	l = k1
	l.extend(k2)
	return l

#adding NOT query
def not_query(k1):
	if project.valid_key(k1):
		f = [i[0] for i in project.mock_data[1:]]
		key = list(set(project.mock_data_dic[k1]))
		for j in key: f.remove(j)
		return project.return_values(f)
	else: return None