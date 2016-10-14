def sum(array):
    max=0;
    till_here=0;
    for i in range(len(array)):
        till_here=till_here + int(array[i]);
        print(till_here);
        if max < 0:
            max=0;
        elif till_here > max:
            max=till_here;
    return max;

n=input("Number of elements you want:");

array=[];

for i in range(int(n)):
    array.append(input("array[i]:"));

print(sum(array));