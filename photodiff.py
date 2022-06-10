import os

ignore = [
    '.picasa.ini',
    '.picasaoriginals',
    '.DS_Store',
    '.DocumentRevisions-V100',
    '.DocumentRevisions-V100-bad-1',
    '.fseventsd',
    '.com.apple.timemachine.donotpresent'
]

def getPaths(base, directory):
    print('Searching', directory)
    paths = []
    dirs = []
    for file in os.listdir(directory):
        if file in ignore:
            continue
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            paths.append(path.replace(base + '/', ''))
        else:
            dirs.append(path)
    for dir in dirs:
        paths += getPaths(base, dir)
    return paths

for volume in [ '/Volumes/Backup1/Photos', '/Volumes/Backup2/Photos' ]:
# for volume in [ '/Volumes/Backup1/Photos' ]:
    name = volume.split('/')[2].lower()
    print(name)
    with open(name, 'w', encoding = 'utf-8') as f:
        paths = getPaths(volume, volume)
        paths.sort()
        for path in paths:
            f.write(path + '\n')
