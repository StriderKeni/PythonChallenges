import re

emails_file = open("emails.txt", "r")
list_emails = []
list_names = []

for line in emails_file:
	list_emails.append((str(line).split()))


for name, email in list_emails:

    if bool(re.match(r"(^|\s)([a-z]+@gmail.com|[a-z]+@[a-z]+gmail.com){1,50}", email)) and bool(re.match(r"^([a-z+]){1,20}", name)):
        list_names.append(name)


list_names.sort()
print('\n'.join(list_names))
