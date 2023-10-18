ls = [ii[:-1] for ii in open('./input.txt', 'r').readlines()]

def new_folder(current, path, folder_name):
    if path.count('/') > 1:
        current[path.split('/')[1]] = new_folder(current[path.split('/')[1]], path[path[1:].index('/')+1:], folder_name)
    if path.count('/') == 1:
        current[path[1:]][folder_name] = {}
    return current

def new_file(current, path, file_name, size):
    if path.count('/') > 1:
        current[path.split('/')[1]] = new_file(current[path.split('/')[1]], path[path[1:].index('/')+1:], file_name, size)
    if path.count('/') == 1:
        current[path[1:]][file_name] = size
    return current

entire = {'main': {}}
path = '/main'
for line in ls:
    if line.startswith('$'):
        if line[2] == 'c':
            if line[5] == '.':
                path = path[:path.rfind('/')]
            else:
                path += '/' + line.split(' ')[2] if line.split(' ')[2] != '/' else ''
    else:
        if line.startswith('dir'):
            entire = new_folder(entire, path, line.split(' ')[1])
        else:
            entire = new_file(entire, path, line.split(' ')[1], int(line.split(' ')[0]))

def find_size(current):
    running = 0
    this_folder = 0
    for item in current:
        if type(current[item]) == int:
            this_folder += current[item]
        else:
            folder_size = find_size(current[item])
            this_folder += folder_size[0]
            if folder_size[0] < 100000:
                running += folder_size[0]
            running += folder_size[1]
    return [this_folder, running]

""" Part 1 """

sz = 0
for folder in entire['main']:
    se = find_size(entire['main'][folder])
    if se[0] < 100000:
        sz += se[0]
    sz += se[1]
print(sz)

""" Part 2 """

nspace = 30000000 - (70000000 - sum([find_size(entire['main'][folder])[0] for folder in entire['main']]))

def smal(current, smallest):
    this_folder = 0
    for item in current:
        if type(current[item]) == int:
            this_folder += current[item]
            if current[item] < smallest and current[item] >= nspace:
                smallest = current[item]
        else:
            folder_size = smal(current[item], smallest)
            if folder_size[0] < smallest and folder_size[0] >= nspace:
                smallest = folder_size[0]
            if folder_size[1] < smallest and folder_size[1] >= nspace:
                smallest = folder_size[1]
            this_folder += folder_size[0]
    return [this_folder, smallest]
    
smallest = 70000000
for folder in entire['main']:
    m = smal(entire['main'][folder], smallest)[1]
    if m < smallest and m >= nspace:
        smallest = m

print(smallest)
