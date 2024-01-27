def NULL_not_found(object: any) -> int:
	if(type(object) == type(None) and not object):
		print(f"Nothing : {object} {type(object)}")
	elif (type(object) == float) :
		print(f"Cheese : {object} {type(object)}")
	elif(type(object) == int and not object):
		print(f"Zero : {object} {type(object)}")
	elif(isinstance(object, str) and not object):
		print(f"Empty : {object} {type(object)}")
	elif(isinstance(object, bool) and not object):
		print(f"Fake : {object} {type(object)}")
	else:
		print("Type not found")
	return 1
