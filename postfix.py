expression = "3 4 + 5 6 + *"

def solve(exp):
	operators = ['+','/','*','-','^']
	stack = [] # FIFO - we will append to end and pop() from end

	for var in exp.split(' '):
		print(var)
		if var in operators:
			v1 = stack.pop()
			v2 = stack.pop()
			try:
				total = op(v1, v2, var)
				stack.append(total)
			except Exception as e:
				print(e)
		else:
			stack.append(int(var))
		print(stack)

def op(v1, v2, op):
	if op == '+':
		return v1+v2
	elif op == '-':
		return v1-v2
	elif op == '*':
		return v1*v2
	elif op == '/':
		return v1/v2
	elif op == '^':
		return v1^v2
	else:
		raise Exception(f'Not implemented for {op}')

solve(expression)




