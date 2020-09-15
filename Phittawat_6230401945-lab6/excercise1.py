tuple1 = (2, 10, 11, 3)
file = []

print("{:50}{}".format("input filenames are", tuple1))

for i in tuple1:
    file_ = "file_{:04d}".format(i)
    file.append(file_)

print("{:50}{}".format("zero padded filenames", file))
print("{:50}{}".format("sorted filenames are", sorted(file)))
