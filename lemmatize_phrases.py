import argparse

parser = argparse.ArgumentParser(usage='Lemmatize list of phrases')
parser.add_argument('phrases')
parser.add_argument('mapping')
args = parser.parse_args()

mapping = {}
for line in open(args.mapping):
    line = line.rstrip()
    form, base = line.split('\t')
    mapping[form] = base

for line in open(args.phrases):
    line = line.rstrip()
    print(mapping.get(line, line))
