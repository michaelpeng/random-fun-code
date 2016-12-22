def minify(path):
    arr = path.split('/')
    return_arr = []
    first = True
    for s in arr:
        if s == "..":
            del return_arr[-1]
        else:
            return_arr.append(s)
    print('/'.join(return_arr))

minify("a/../b/../c")