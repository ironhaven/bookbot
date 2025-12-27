def get_nums_words(text):
    return len(text.split())

def charater_count(text):
    counter = {}
    for c in text:
        c = c.lower()
        if not c.isalpha():
            continue
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter

def sorted_counts(counts):
    dicts = []
    for k, v in counts.items():
        dicts.append({
            "char": k, "num": v
        })

    dicts.sort(reverse=True, key=lambda x: x["num"])
    return dicts
