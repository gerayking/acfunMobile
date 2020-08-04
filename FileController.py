

def save(filename:str,content):
    f =open(filename,"w+")
    f.write(str(content))
    f.close()

def read(filename:str):
    f = open(filename,"r")
    res_str = f.read()
    f.close()
    return res_str

def read_dict(filename:str):
    f = open(filename,"r")
    res = eval(f.read())
    f.close()
    return res;