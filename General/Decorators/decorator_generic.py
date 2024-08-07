

def my_function(function):
    def wraped_function(): # funcaiton inside other function (inner function)
        print("Isso e executado antes")
        function()
        print("Isso e executado depois")
    return wraped_function()


@my_function
def funcao1():
    print("Isso sera executado no meio")
    return "Hi"

def funcao2():
    print("I called function 2 without ")

my_function(funcao2)

funcao1
