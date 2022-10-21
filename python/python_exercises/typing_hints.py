import typing

t: typing.Tuple[int, int, int] = [1, 2, 3] # use Tuple if u want to specify 
                                           #the type of every element in the type

# sequence from typing module is anything that can be indexed
def print_sequence_elements(sequence: typing.Sequence[str]):
    for i, s in enumerate(s):
        print(f"item {i}: {s}")


# Optional from typing module use for hinting because it has a default value
def foo(format_layout: typing.Optional[bool] = True):
    ...


# Callable is what you use when you want to use a function as an argument.
def foo(x: int, y: int, func: typing.Callable) -> int:
    output = func(x, y)
    return output


#TypedDict allows you to declare a dictionary type that expects all of its 
# instances to have a certain set of keys, 
# where each key is associated with a value of a consistent type.
class MyDictType(typing.TypedDict):
    name: str
    interests: typing.List[str]


#TypedDict allows you to declare a dictionary type that expects all of 
# its instances to have a certain set of keys, where each key is associated 
# with a value of a consistent type.
my_dict_type = typing.Dict[str, str]


#List type is that it can hold any type inside it, not the built-in ones only.
#  Our own types can basically be combined with List.
def my_dummy_function(vector: typing.List[float]):
   return sum(vector)