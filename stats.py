def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

def count_characters(text):
    text = text.lower()
    counts = {}
    for c in set(text):
        counts[c] = text.count(c)
    return counts

def sort_on(dict):
    return dict["count"]

def sort_most_frequent(counts):
    output = []
    for char in counts:
        output.append({"char" : char, "count": counts[char]})
    output.sort(reverse=True, key=sort_on)
    return output