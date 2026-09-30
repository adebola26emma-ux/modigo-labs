def top_words(text, n):
    # TODO: count word frequency (case-insensitive), then return the top `n`
    # as (word, count) tuples sorted by count descending, ties broken alphabetically
    text = text.lower()
    words = text.split()
    counted_words = {}
    for word in words:
        if word not in counted_words:
            counted_words[word] = 0
        counted_words[word] += 1
    counted_words = dict(sorted(counted_words.items()))
    result = []
    for i in range(1, n+1):
        highest = 0
        most = ''
        for word, count in counted_words.items():
            if count > highest:
                highest = count
                most = word
        if i <= len(counted_words)+len(result):
            result.append((most, highest))
            counted_words.pop(most)
    return result
            

print(top_words("the cat sat on the mAT THE CAT RAN", 4))
print(top_words('', 3))
