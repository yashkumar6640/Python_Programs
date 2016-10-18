def main():
	n, d=input().split();
	n, d=[int(n), int(d)];
	x=[];
	x.extend(input().split());
	x=[int(i) for i in x];
	while d>0:
		y=x[0];
		x.remove(x[0]);
		x.append(y);
		d=d-1;
	for i in x:
		print(i, end=" ");

main();
