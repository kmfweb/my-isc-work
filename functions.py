'''
def double_it(number):
    return(2 * number)
    
print(double_it(2))
print(double_it(2.2))
print(double_it("hello"))
'''

def calc_hypo(a, b):
    if ((type(a) and type(b)) in (int, float)) and  a >= 0 and b  >=0:
        print("a and be are either of type float or int, and positive numbers.")
        c = (a*a + b*b)**0.5
        return(c)
    else:
        print("A string cannot be calculates, neither 0 or a negative number can.")
        return(False)
	
print(calc_hypo(-3, 4))


