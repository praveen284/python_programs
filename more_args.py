# these are multiple positional arguments

def more_args(*args):
	print(args)

more_args(1,2,3,4)
more_args(1,2,3,4,5,6,7,8,9,0)
more_args()

def greet(arg_1,arg_2):
	print(arg_1 + " " + arg_2)

data = ["Hello","Praveen"]
greet(*data)


# these are multiple keyword arguments

def more_kwargs(**kwargs):
	print(kwargs)

more_kwargs(a=1,b=2,c=3)
more_kwargs(a=1,b=2,c=3,g=7)
more_kwargs()

def greet(kwarg_1="Hi",kwarg_2="Ram"):
	print(kwarg_1 + " " + kwarg_2)

data = {"kwarg_1":"Hello","kwarg_2":"Praveen"}
greet(**data)