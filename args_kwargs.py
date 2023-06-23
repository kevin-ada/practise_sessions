# Args and kwargs
# What you need to know is that args is a infinite tuple while kwargs is an infinite dictionary


def add_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_numbers(1, 2, 3, 4, 5, 5, 6, 7, 8, 8))


def list_of_strings(*args):
    for name in args:
        print(name, end=' ')


list_of_strings('Dr', 'jim', 'Brantford')

print()


# Kwargs

def country_capital(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

    for value in kwargs.values():
        print(value)


country_capital(Kenya='Nairobi', Uganda='Kampala')
