from os import remove


def create(file_name):
    with open(f'./resources/{file_name}', 'w') as file:
        file.write('')


def add(file_name, content):
    with open(f'./resources/{file_name}', 'a') as file:
        file.write(content + '\n')


def file_replace(file_name, old_string, new_string):
    try:

        content = ''

        with open(f'./resources/{file_name}', 'r') as file:

            list_of_lines = file.readlines()
            for line in list_of_lines:
                content += line.replace(old_string, new_string)

        with open(f'./resources/{file_name}', 'w') as file:

            file.write(content)

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        remove(f'./resources/{file_name}')
    except FileNotFoundError:
        print("An error occurred")


while True:

    command = input().split('-')

    if command[0] == 'End':
        break

    if command[0] == 'Create':
        file_name = command[1]

        create(file_name)

    elif command[0] == 'Add':
        file_name = command[1]
        content = command[2]
        add(file_name, content)


    elif command[0] == 'Replace':
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        file_replace(file_name, old_string, new_string)



    elif command[0] == 'Delete':
        file_name = command[1]

        delete_file(file_name)
