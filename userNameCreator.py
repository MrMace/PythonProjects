firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')

userName = firstName[0] + lastName[:7]
userName = userName.lower()

print("Your username is", userName)