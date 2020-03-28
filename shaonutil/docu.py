import ast

def show_info(functionNode):
    print("Function name:", functionNode.name)
    print("Args:")
    for arg in functionNode.args.args:
        #import pdb; pdb.set_trace()
        print("\tParameter name:", arg.arg)


filename = "imgcode.py"
with open(filename) as file:
    node = ast.parse(file.read())

functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

for function in functions:
    show_info(function)

for class_ in classes:
    print("Class name:", class_.name)
    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
    for method in methods:
        show_info(method)