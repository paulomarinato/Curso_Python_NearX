def soma(x: int, y: int = 98) -> int:
    return x + y

def soma2(primeiro: int, *args: list[int]) -> int:
    print(primeiro)
    return sum(args)

def soma3(**kwargs: dict[any, any]) -> int:
    
    return kwargs["x"] + kwargs["y"]

z = soma(x=3, y=97, e=889)

print (z)