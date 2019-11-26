def mean(li):
	# avearage or mean of elements
	return sum(li)/len(li)

def median(li):
	# median of elements 
	n = len(li) 
	li.sort() 

	if n % 2 == 0: 
		median1 = li[n//2] 
		median2 = li[n//2 - 1] 
		median = (median1 + median2)/2
	else: 
		median = li[n//2] 

	return median



if __name__ == '__main__':
	pass