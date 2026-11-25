def add(a:float, b:float) -> float|None:
    return a + b

def subtract(a:float, b:float) -> float|None:
    return a - b

def multiply(a:float, b:float) -> float|None:
    return a * b

def divide(a:float, b:float) -> float|None:
    if b == 0:
        return
    return a / b