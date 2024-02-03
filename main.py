def print_hello_world():
    print("Hello world")

def vivaMechMat():
    print("Viva Mech-mat faculty!!!")

def print_tree():
    size = 10

    for i in range(size):
        for j in range(size - i):
            print(' ', end='')
        for j in range(2 * i + 1):
            if j % 2 == 0:
                print('*', end='')
            else:
                print('-', end='')
        print()

    for i in range(size // 2):
        for j in range(size - 1):
            print(' ', end='')
        print('| |')

for i in range(10):
    print_hello_world()

vivaMechMat()
print_tree()