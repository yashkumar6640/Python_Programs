def longest_subsequence_length(string1, string2):
	print(len(string1), len(string2));
	matrix=[];
	for i in range(len(string1) + 1):
		matrix.append([]);
		for j in range(len(string2) + 1):
			matrix[i].append(0);
	for i in range(len(string1) + 1):
		for j in range(len(string2) + 1):
			if i==0 or j==0:
				matrix[i][j]=0;
			
			elif string1[i-1]==string2[j-1]:
				matrix[i][j]=matrix[i-1][j-1]+ 1;
			else:
				matrix[i][j]=max(matrix[i-1][j], matrix[i][j-1]);

	for i in range(len(string1) + 1):
		print(matrix[i]);
	return matrix[len(string1)][len(string2)];



def main():
	string1, string2=input().split();

	print(longest_subsequence_length(string1, string2));

main();