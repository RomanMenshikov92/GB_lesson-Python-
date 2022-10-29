
def get_list(n, f):
    list_full = []
    for i in f:
        list_full.append(i.split()[n])
    return list_full


def sort(n, f):
    list_full = []
    for i in f:
        if n in i:
            list_full.append(i)
    return list_full
