# Always advisable to use the context manager while reading files

with open('new_file.txt', 'r') as f:

    size_to_read = 15


    file_opened = f.read(size_to_read)
    print(file_opened, end=' ')

    f.seek(5)

    file_opened = f.read(size_to_read)
    print(file_opened, end=' ')


with open('main.py') as file:
    for lines in file:
        print(lines)



# Copying an image file

with open('night.png', 'rb') as night_file:
    with open('night1.png', 'wb') as ng1:
        for image in night_file:
            ng1.write(image)






