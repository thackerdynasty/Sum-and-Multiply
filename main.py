ans = 0
lis = [1,2,3,4]
def sum(l):
	global ans
	for i in range(len(l)):
		if i == 0:
			ans = l[i]
		else:
			ans += l[i]
	return ans
print(sum(lis))
