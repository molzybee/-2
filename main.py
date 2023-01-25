import random
a = []
def work():
    alfavit = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuWwXxYyZz1234567890%/@#'
    count = int(input("Введите желаемое количество сгенерируемых паролей: "))
    len = int(input("Введите длину этих паролей: "))
    for i in range(count):
        password = ''
        for i in range(len):
            password += random.choice(alfavit)
        a.append(password)
        new_file = open("password.txt", 'w')
        for r in a:
            new_file.write(r + '\n')
    print("Ваши пароли лежат в файле password.txt")
if __name__ == "__main__":
    work()

