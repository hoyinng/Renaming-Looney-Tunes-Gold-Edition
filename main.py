import os
from functools import reduce
import re

# Added to match files renamed by the author
corrections = {
    'message to gracias, a ntsc dvd-jch' : 'A Message To Gracias',
    'senorella and the glass huarache': 'Señorella and the Glass Huarache',
    'the awful orphan': 'Awful Orphan',
    'all abir-r-r-d': 'All a Bir-r-r-rd',
    'tweetie pie': 'Tweety Pie',
    'daffy duck and egghead' : 'Daffy Duck & Egghead'
}

sep = os.path.sep

src = "Y:\\Movies\\Temp\\Looney.Tunes.S01-S24.Golden.Collection.DVDRip"
dst = "Y:\\Movies\\Temp\\Looney Tunes Golden Collection"

def betterlistdir (root):
    return [os.path.join(root,path) for path in os.listdir(root)]

p = list(filter(lambda x : x.startswith('Volume'), os.listdir(dst)))
p = list(map (lambda x : list(filter(lambda y : y.endswith('mkv'), betterlistdir(os.path.join(dst,x)))), p))
p = reduce(lambda a,b: a+b,p,[])

s = list(filter(lambda x: x.startswith('Looney Tunes Season'), os.listdir(src)))
s = list(map (lambda x : list(filter(lambda y : y.endswith('mkv'), betterlistdir(os.path.join(src,x)))), s))
s = reduce(lambda a,b: a+b,s,[])

for file in s:
    f = ' '.join(''.join(file.split(sep)[-1:]).strip('.mkv').split(' ')[1:])
    r = ([a for a in p if re.sub('[^a-zA-Z]+', '', f.lower()) in re.sub('[^a-zA-Z]+', '', a.lower())])
    if (len(r) > 1 or len(r) == 0):
        # fix for filename being slightly off
        if (f.lower() in corrections.keys()):
            f = corrections.get(f.lower())
        elif ('-' in f):
            f = f.replace('-','')
        r = ([a for a in p if f.lower() in a.lower()])
        if (len(r) > 1 or len(r) == 0):
                print ('cannot match {}'.format(file))
                print ('best guess', ([a for a in p if f.lower().split()[-1] in a.lower()]) )
                break
    i = (os.path.join(src,file))
    r = os.path.join(dst,r[0])
    print (i + ' > ' + r)
    # Uncomment below to run
    #os.replace(i,r)




