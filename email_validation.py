import re

if __name__ == '__main__':
	
	list_emails = [] # list with all cases of name and email
	valid_mails = [] # this list contain only valid emails with his name

	for _ in range(int(input())):
		str1 = input()
		list_emails.append(str1.split()) 

	for name, email in list_emails:
		match = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email)
		if match != None:
			valid_mails.append((name, email))
			print(name + ' ' + email)




	#print(' '.join([name[1] for name, email in valid_mails]))



