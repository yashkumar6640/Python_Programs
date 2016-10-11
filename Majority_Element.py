def majorityElement(array):
	count=0;
	maj_index=0;
	n=len(array)-1;
	for i in range(n):
		if(array[i]==array[maj_index]):
			count=count+1;
		else:
			count=count-1;
		if(count==0):
			maj_index=i;
			count=1;
	return array[maj_index];
		


n=input("Enter the number of elements you want in your array:");
array=list();
for i in range(int(n)):
	value=input("array[i]:");
	array.append(int(value));
for i in range(int(n)):
	print(array[i]);
print("The majority Element is :", majorityElement(array));


