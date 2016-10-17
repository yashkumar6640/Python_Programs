def check(c):
	if type(c)==str:
		x=c;
		x=x[:-1];
		x=int(x);
		return x;
	else:
		return c;
def last_char(c):
	return c[-1:];
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            L[i][j] = 0;
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0;
            if i!=0 and j!=0:
            	if X[i-1]==Y[j-1]:
            		if type(L[i-1][j-1])==str:
            			q=L[i-1][j-1];
            			q=q[:-1];
            			q=int(q);
            			L[i][j]=q+1;
            		else:
            			L[i][j]=L[i-1][j-1] + 1;

            		
            	else:
            		if type(L[i-1][j]) == str:
            			x=L[i-1][j];
            			x=x[:-1];
            			x=int(x);
            		if type(L[i][j-1])==str:
            			y=L[i][j-1];
            			y=y[:-1];
            			y=int(y);
            		if type(L[i-1][j]) == int and type(L[i][j-1])==int:
            			if L[i-1][j] > L[i][j-1]:
            				L[i][j]=str(L[i-1][j]) + 'u';
            			else:
            				L[i][j]=str(L[i][j-1]) + 'l';
            		if type(L[i-1][j])==str and type(L[i][j-1])==str:
            			if x > y:
            				L[i][j]=str(x) + 'u';
            			else:
            				L[i][j]=str(y) + 'l';
            		elif type(L[i-1][j])==str:
            			if x >L[i][j-1]:
            				L[i][j]=str(x) + 'u';
            			else:
            				L[i][j]=str(L[i][j-1]) + 'l';
            		elif type(L[i][j-1])==str:
            			if y > L[i-1][j]:
            				L[i][j]=str(y) + 'l';
            			else:
            				L[i][j]=str(L[i-1][j]) + 'u';
    

    p=m;
    s=n;
    string=[];
    while p >= 1 and s >=1:
    	if type(L[p][s]) ==int and L[p][s]==check(L[p-1][s-1]) + 1:
    		string.append(Y[s-1]);
    		p=p-1;
    		s=s-1;
    	else:
    		l=last_char(L[p][s]);
    		if l == 'u':
    			p=p-1;
    		else:
    			s=s-1;

    string.reverse();
    string=[int(i) for i in string];
    i=0;
    for i in string:
    	print(i, end=" ");








            				
	   
         
    # if type(L[m][n])==str:
    # 	k=L[m][n];
    # 	k=k[:-1];
    # 	k=int(k);
    # 	return k;
    # return L[m][n];


def main():
    n, m = input().split();
    n = int(n);
    m = int(m);

    str1 = [int(n) for n in input().split()];
    str2 = [int(n) for n in input().split()];

    lcs(str1, str2);


main();