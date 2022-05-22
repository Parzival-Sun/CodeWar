import re

def pig_it(text):
    output = []
    # TODO 1: Slide to words
    split_text = text.split()
    # TODO 2: Use regex to find the first char of word is a-z|A-Z
    for word in split_text:
        r1 = re.findall(r"^\w", word)
    # TODO 3: Move the first char to the end of the word and add "ay"
        if r1:
            output.append(word[1:] + word[0] + "ay")
        else:
            output.append(word)
    # TODO 4: re-integrate to a sentence
    return " ".join(output)


def re_test(test_str):
    r1 = re.findall(r"^\w+", test_str)
    print(r1)


print(pig_it("Pig latin is cool"))
print(pig_it("Hello world !"))
re_test("guru99,education is fun")
re_test("Ponson Test 1")
re_test("$#@ PonsonTest 2")


