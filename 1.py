import fileinput

freqs = []
for line in fileinput.input():
    freqs.append(int(line.strip()))

print(sum(freqs))
