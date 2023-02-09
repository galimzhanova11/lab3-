n=list(map(int, input("elements of array:-").strip().split()))
odd=list(filter(lambda x:(x%2!=0),n))
print(odd)