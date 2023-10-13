alpha, ring = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []

def gen_second_dial(num):
    counter = 0
    for _ in range(26):
        counter += num - 1
        while counter > len(alpha) - 1:
            counter -= len(alpha)
        ring.append(alpha.pop(counter))

        
num, string = input().split()
gen_second_dial(int(num))
final = []
print("".join(ring[:6]))

for letter in str(string):
    final.append(ring[ord(letter)-65])
    ring.append(ring.pop(0))
    
print("".join(final))