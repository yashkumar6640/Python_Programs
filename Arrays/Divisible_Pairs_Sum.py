def main():
	n, k=input().split();
	n=int(n);
	k=int(k);
	array=[];
	array.extend(input().split());	
	array=[int(i) for i in array];	
	c=0;
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if (array[i] + array[j]) % k == 0:
				c=c+1;

	print(c);

main();
