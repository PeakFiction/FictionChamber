def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def greeting():
    return 'Hello!'
greeting = uppercase_decorator(greeting)

greeting()