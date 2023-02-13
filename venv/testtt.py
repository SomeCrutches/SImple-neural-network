
#
# def count_lines(filename, chunk_size=1<<13):
#     with open(filename, encoding="utf-8") as file:
#         return sum(chunk.count('\n')
#                    for chunk in iter(lambda: file.read(chunk_size), ''))
#
#
#
#
#
# with open("Unost.txt", "r+", encoding='utf-8') as file:
#     for i in range(count_lines("Unost.txt") + 1):
#         line = file.readline()
#         print(line)

f=open("Unost.txt", "r+", encoding='utf-8').readlines()
n = 128
i = 0
while i < n:
    print (f[i])
    print(i)
    j = f[i].split()
    if len(j) != 2:
        f.pop(i)
        n-=1
        buff = True
    for p in range(len(j)):
        if j[p].find("[") != -1 and buff == False:
            f.pop(i)
            n-=1
    i+=1
    buff = False
print(f)

