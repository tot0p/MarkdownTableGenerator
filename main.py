

from MDTable import *

if __name__ == '__main__':
    test = Table(header=['Name', 'Age'], data=[['John', 20], ['Jane', 21]])
    test.add_row(['Jack', 22])
    test.add_column("last name", ["Doe", "Doe", "Doe"])
    test.add_column("first name", ["John", "Jane", "Jack"])
    print(test)
