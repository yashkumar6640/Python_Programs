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
				
array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
sum=13;
checkSum(array, sum);

