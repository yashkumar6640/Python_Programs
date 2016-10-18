def main():
	n=input();
	n=int(n);
	contacts={};
	result=[];
	contacts=dict(input().split() for _ in range(n));
	try:
		while True:
			inp=input();
			if inp != "":
				if inp in contacts:
					result.append(inp+"="+contacts[inp]);
				else:
					result.append('Not found');
					
			else:
				break;
	except EOFError:
		pass;
	for i in result:
		print(i);

main();