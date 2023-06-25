import os

"""Working with the OS module in Python"""


"""Get the process Id"""
print(os.getpid())

"""get the current working directory using the module"""
print(os.getcwd())


"""change working directory using the module"""
os.chdir('/Users/Admin/PycharmProjects/')


"""Works like LS in a linux distro"""
print(os.listdir())


"""get the current working directory using the module"""
print(os.getcwd())

os.chdir('/Users/Admin/PycharmProjects/practise_sessions')

print(os.getcwd())


"""Using the Module to Create Directories and Subdirectories"""
os.makedirs('test/test.txt')

os.renames('test/test.txt', 'hello/hello.txt')


"""Using the Module to Remove Directories and Subdirectories"""
os.removedirs('hello/hello.txt')

"""Using the walk attribute to traverse a file"""


for path, dirname, dirfiles in os.walk('/Users/Admin/PycharmProjects/practise_sessions/'):
    print(path)
    print(dirname)
    print(dirfiles)
    print()

print(os.environ.get('HOME'))
