def anagrams(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))


def main():
    word1, word2 = input(), input()
    res = anagrams(word1, word2)
    print("Anagrams") if res is True else print("Not anagrams")


main()
