import collections
import bz2

stats=collections.defaultdict(lambda: collections.defaultdict(int))

def increment(buffer):
    form=' '.join([x[1] for x in buffer])
    base=' '.join([x[2] for x in buffer])
    stats[form.lower()][base.lower()]+=1

path='tokens-with-entities-and-tags.tsv.bz2'
path='/net/scratch/people/plgapohl/wiki/pl/2019/tokens-with-entities-and-tags.tsv.bz2'
with open('autophrase_train.txt','wt') as f:
    buffer=[]
    # for line in open(path):
    for line in  bz2.open(path, 'rt'):
        line=line.rstrip()
        fields = line.split('\t')
        if len(fields)!=7:
            f.write('\n')
            continue

        if '/' not in fields[2]:
            f.write(fields[2].lower()+'/'+fields[4].split(':')[0]+' ')

        if fields[5]=='_':
            if buffer:
                increment(buffer)
                buffer=[]
        else:

            this=(fields[5], fields[1], fields[2])
            if not buffer or buffer[-1][0]==this[0]:
                buffer.append(this)
            else:
                increment(buffer)
                buffer=[this]
    if buffer:
        increment(buffer)




with open('phrases_lemmas.tsv','wt') as f:
    for k,v in stats.items():
        # print(k)
        best=sorted(v.items(), key=lambda x: x[1], reverse=True)[0]
        # for k2, v2 in v.items():
        #     print('-', k2, v2)
        # print('\t'.join([k, best[0]]))
        f.write('\t'.join([k, best[0]]))
        f.write('\n')
