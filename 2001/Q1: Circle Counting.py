def find_last_person(n, k):
    people, pointer = list(range(1, n+1)), 0
  
    while len(people) > 1:
        pointer += (k-1) % len(people)
        if pointer > len(people) - 1:
            pointer -= len(people)
        people.pop(pointer)
    return people[0]

def main():
    n, k = int(input()), int(input())
    print(find_last_person(n, k))

main()
