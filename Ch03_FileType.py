fp = open("sample.txt", "w")

fp.write("Sample Text.")

print(type(fp))
print(fp)

fp.close()

file = open("sample.txt", "a")
file.write("\nThis is line 2")
file.close()
