import re

def n_gram(arr, n):
    return zip(*(arr[_:] for _ in range(n)))

d = dict()
with open("Extra Material 2 - keyword list_with substring.csv") as f:
    f.readline()
    for line in f:
        line = line.split(',')
        grp, words = int(line[0]), line[1:]
        for w in words:
            w = w.strip('" \n').lower()
            if w in d:
                d[w] = min(d[w], grp)
            else:
                d[w] = grp

out_file = "index,groups_found\n"
with open("Keyword_spam_question.csv", encoding="utf8") as f:
    f.readline()
    for line in f:
        line = line.split(',')
        idx, line = int(line[0]), ''.join(line[1:])
        line = re.sub(r'[^a-z0-9]', ' ', line.strip().lower())
        line = re.sub(r'[ ]+', ' ', line.strip())

        arr = line.split(' ')
        print(idx)
        # print(arr)

        length = len(arr)
        out = set()
        while length > 0:
            # print(f"Length {length}")
            for gram in n_gram(arr, length):
                key = ' '.join(gram)
                if key in d:
                    out.add(d[key])
                    line = line.replace(key, '')
                    line = re.sub(r'[ ]+', ' ', line)
                    arr = line.split(' ')
                    # print(key, arr)
            length -= 1
            if len(arr) < length:
                length = len(arr)
        # print(sorted(out))
        if len(out) == 1:
            out_file += f'{idx},{list(out)}\n'
        else:
            out_file += f'{idx},"{sorted(out)}"\n'

with open("out.csv", 'w', encoding="utf8") as f:
    f.write(out_file)
print("done")