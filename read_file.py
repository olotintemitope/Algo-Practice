f = open('sample_text.txt', 'r')
file_data = f.read()
f.close()

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())