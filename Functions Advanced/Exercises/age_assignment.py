def age_assignment(*args, **kwargs):

    age_dict = {}

    for key in kwargs:
        for name in args:
            if name.startswith(key):
                age_dict[name] = kwargs[key]


    final_result = ''

    for key,value in sorted(age_dict.items(), key=lambda x: x[0]):
        final_result += f'{key} is {value} years old.\n'

    return final_result

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))