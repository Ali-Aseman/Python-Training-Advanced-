# function
# a statement(s) which has a special duty.

# 1. reusability
# 2. break down code into logical section
# 3. ...

# def function_name(params):
#   code section
#   code block
#   return statement

# inputs: 0 or unlimited
# outpus: 1 or unlimited

# Python Docstring Generator


def adder(a, b):
    """ [1]
    docstring
    """
    return a + b


def simple_functinon(a , b):
    """ [2]
    This is a simple function which add two numbers.

    Args:
        a (int): a number
        b (int): a number
    """
    pass

def simple_functinon2(a , b):
    """[3]
    [GHOSTEPROG]

    Args:
        a ([type]): [description]
        b ([type]): [description]

    Returns:
        [type]: [description]
    """
    return a + b


def GHOSTEPROG(c, d):
    """
    [GHOSTEPROG => 4]

    Args:
        a ([type => 4]): [|]
        b ([type] => 4): [|]

    Returns:
        [type]: [|]
    """
    return c + d
    
print(adder.__doc__) # [1]
print(simple_functinon.__doc__) # [2]
print(simple_functinon2.__doc__) # [3]
print(GHOSTEPROG.__doc__)

methods = [adder, simple_functinon, simple_functinon]

with open("doc.txt", "w") as file:
    for method in methods:
        file.write(method.__doc__ + "\n")

# 
html = "<html><body>" 
for method in methods:
    html += f"<h1>{method}</h1><p>{method.__doc__}</p>"

html += "</body></html>"

with open("doc.html", "w") as file:
    file.write(html)
