# The special syntax *args in function definitions in python
# is used to pass a variable number
# of arguments to a function. It is used to pass a non-key worded,
# variable-length argument list.


# The special syntax **kwargs in function definitions in python is used to
# pass a keyworded, variable-length argument list.



def fun(*vals):
    for arg in vals:
        print(arg)
fun("hey",'man','How',123,'You')

def funnier(**kvals):
    for karg in kvals:
        print(karg,kvals[karg])
funnier(First="1",sec='Two',Thrid='Three')