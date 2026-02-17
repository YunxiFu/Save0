def judgement():
	"""
	用于判断田地是否可以收割的代码，可以返回1，不可以返回0
	"""
	if can_harvest():
		harvest()
		return 1
	else:
		return 0	
