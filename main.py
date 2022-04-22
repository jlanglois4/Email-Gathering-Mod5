import re

from email import Email

domains = []
regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"

while len(domains) != 5:
    email = input("Enter email address: ")
    try:
        domain = re.search(regex, email)
        email = Email(domain.group())
        domain_check = email.get_domain()
        print(domain_check)
        domains.append(domain_check)
    except AttributeError:
        print("Invalid email address.")
print(' '.join(domains))
