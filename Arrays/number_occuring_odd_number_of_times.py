def find_num(array):
	number=0;
	for i in array:
		number = number ^ i;
	return number;

array=[1,2,1,2,3,4,3];
print(find_num(array));