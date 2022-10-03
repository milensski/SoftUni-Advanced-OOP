import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooManyAtSymbolsError(Exception):
    pass


domains = ['.com', '.bg', '.org', '.net']

pattern_name = r'(\w+)'

pattern_domain = r'(\.[a-z]+)'

name = ''

while True:

    read_email = input()

    if read_email == "End":
        break

    name = re.search(pattern_name, read_email)
    domain = re.search(pattern_domain, read_email)

    try:

        if len(name.group()) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')

        if read_email.count('@') > 1:
            raise TooManyAtSymbolsError('Too many @ symbols')

        elif read_email.count('@') < 1:
            raise MustContainAtSymbolError("Email must contain @")

        if domain.group() not in domains:
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(domains)}')

        print(f'Email is valid')

    except AttributeError:

        print(f'Invalid email')