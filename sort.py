def get_dat(n, f):
    lst = []
    for i in f:
        lst.append(i.split()[n])
    return lst

def sort(n, f):
    lst = []
    for i in f:
        if n in i:
            lst.append(i)
    return lst

