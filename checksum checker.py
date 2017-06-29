print('Checksum Checker v1.0\n')

check_one = input('Enter first checksum:\n\n')
check_two = input('\nEnter second checksum:\n\n')

if check_one.strip() == check_two.strip():
	print('\nSuccess! Matching checksums')
else:
	print('\nDid not match. Re-download the file.')
	
input('\nPress a key to exit')
