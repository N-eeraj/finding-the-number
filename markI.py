max,min=100,1
lst=list(range(min,max+1))

print('Think a number between 1 & 100\n')

try:
	for i in range(7):
		print('Chances :',7-i)
		try:
			guess=lst[len(lst)//2]
		except:
			print('\tCheater!!')
			exit()

		while(True):
			x=input('Is the number : '+str(guess)+' (Y/N)').lower()

			if(x=='y'):
				print('\nI Won!')
				exit()

			elif(x=='n'):
				while(True):
					change=input('Is the number Greater or Smaller? (G/S)').lower()

					if(change=='g'):
						lst=list(filter(lambda x: x>guess,lst))
						break

					elif(change=='s'):
						lst=list(filter(lambda x: x<guess,lst))
						break

					else:
						print('Enter Valid Output\n')
				break

			else:
				print('Enter Valid Output\n')
	print('\nI Lost')

except:
	print('\n\nExiting')
