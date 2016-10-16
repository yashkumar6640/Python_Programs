def find_max(matrix, n):
	mat=[];
	for i in range(n):
		mat.append([]);
		for j in range(n):
			mat[i].append(0);
	for i in range(n):
		for j in range(n):
			if matrix[i][j]==0:
				continue;
			else:
				mat[i][j]=matrix[i][j];
				if i==0:
					mat[i][j]=matrix[i][j];
				if j==0 and i!=0:
					mat[i][j]=int(mat[i][j])+int(mat[i-1][j]);
				else:
					mat[i][j]=int(mat[i][j])+max(int(mat[i-1][j]), int(mat[i-1][j-1]));
	return mat[n-1];
def main():
	matrix=[];
	t=input();
	n=input();
	s=int(n);
	for i in range(s):
		matrix.append([]);
		for j in range(s):
			if(j<=i):
				matrix[i].append(input());
			else:
				matrix[i].append(0);
	print(matrix);
	print(max(find_max(matrix,s)));
main();