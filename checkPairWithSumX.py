def checkSum(array, sum):
	i=len(array)-1;
	j=0;
	while(j<i):
		if(array[i]+array[j] > sum):
			i=i-1;
		elif(array[i] + array[j] <sum):
			j=j+1;
		else:
			print("low_index=", j, "high_index=", i, "and array[i] + array[j]=", array[i] + array[j]);
			break;
	if(j>=i):
		print("No such pair");
n=input("Enter the limit of array");
print(n);
array=list();
for i in range(int(n)):

	index=input("num:");
	array.append(int(index));
array.sort();			
sum=13;
checkSum(array, sum);

