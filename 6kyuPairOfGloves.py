from collections import Counter
def number_of_pairs(gloves):
    counts = Counter(gloves)
    total = 0
    for key in counts:
        total += (counts[key] // 2)
    return total




print(number_of_pairs([]))
print(number_of_pairs(["red","red"]))
print(number_of_pairs(["red","green","blue"]))
print(number_of_pairs(["gray","black","purple","purple","gray","black"]))
print(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]))