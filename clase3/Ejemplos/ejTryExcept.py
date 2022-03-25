try:
	n = int(input("ingrese numero: "))
	print(f"para N = {n} el inverso es = {1/n}")
	exit()
except ValueError as e:
	print(f"error: {e} type: {type(e)}")
except ZeroDivisionError as e:
	print(f"error: {e} type: {type(e)}")
except Exception as e:
	print(f"error: {e} type: {type(e)}")
#except: ### NO HACER ###
#	print(f"error: {e} type: {type(e)}")
