---
title: Python Package Best Practices: Using Type Hints
layout: post
tags: python type-hints software-engineering
---

# Type Hints

## Allow for Any Type

### "Any" as in "Anything Goes!"
If an input may truly be any type without restriction, then use
the `Any` type, e.g.:

```python
def fcn(x: Any): return x
```

Similarly, a function might accept two lists, each of which
contain values of a single type, but with no further constraint
on what those types might be. 

```python
def fcn(x: List[Any], y: List[Any]):
  # do stuff
  return output
```


### "Any" as in "Consistently Any"
You can also use `TypeVar` to construct an "any" type.

```python
from typing import TypeVar
AnyType = TypeVar('AnyType')
```

This might seem redundant with `Any` at first glance. However, the 
`Any` type truly allows for anything, while `TypeVar('A')` (or
any `TypeVar('NameMe')` you define) provides a little more control (w.r.t. a 
static type checker; not at runtime).  For example, if a specific input 
can be of any type but should be consistent with the type of some other
input, then using type hints that are slightly more restrictive than 
`Any` can be used with this `TypeVar` technique, e.g.:

```python
Type1 = TypeVar('Type1')
Type2 = TypeVar('Type2')

def fcn(
    x1: Type1, 
    x2: Type1, 
    y1: Type2, 
    y2: Type2
):
    return (x1,x2), (y1,y2)
```

The `TypeVar` version of `Any` can often be more illuminating to those 
unfortunate souls who must read over your code.

For example, it might be helpful to know that a function that accepts
a single input of any type will return an output of the same type.  

```python
T = TypeVar('T')
def fcn(x: T) -> T:
  # do stuff
  return output
```

Similarly, a function might accept two lists, each of which
contain values of a single type, but with no further constraint
on what those types might be. Though you can use `Any` here, it might 
be desirable to add some metadata.

```python
Whatever = TypeVar('Whatever')
Anything = TypeVar('Anything')

def fcn(x: List[Whatever], y: List[Anything]):
  # do stuff
  return output
```




## Allow for One of Multiple Types
Sometimes you want flexibility, but not just "any" flexibility.  

### TypeVar
`TypeVar` can be used to specify that multiple possible types are allowed,
e.g., `TypeVar('StrFlt',str,float)` allows for string or float. 


### TypeVar Use-Case Example
Here is a pretty good use case I came up with.  It uses `TypeVar` as a 
way to (i) define "Any" type vars that have a specific purpose and must
be used consistently, and (ii) define lightly-restrictive vars that allow
for some-but-not-all types.

```python
from typing import TypeVar,Tuple,Sequence,List  #,Dict
Key = TypeVar('Key')
Val = TypeVar('Val')
MultiKey = TypeVar('MultiKey',Key,Sequence[Key])

class MultiKeyDict(dict):
    def __getitem__(self, keys: MultiKey) -> List[Val]:
        if isinstance(keys,Tuple):
            vallist = list()
            for key in keys: 
                vallist.append(self.get(key))
            return vallist
        else: 
            return self.get(keys)
```

### More of my unprocessed notes on TypeVar
Wrote these down on using `Generic` and possibly creating generic TypeVars, 
but not certain on the info... Will learn a bit more before integrating 
this info into a narrative flow....

* Generic TypeVars (pros)
  - allows an Any-like behavior but w/ constraint
  - e.g., `(Any, Any) -> Any` allows literally any combo, such as `(int, bytes) -> str`;
    however, if `AnyT = TypeVar('AnyT')`, then `(AnyT, AnyT) -> AnyT` will only 
    allow things like `(int, int) -> int` or `(str, str) -> str`
  - gives your custom type a __getitem__ check


## NewType for MetaData and Consistency

Sometimes you just want to provide some metadata about an
input, but not necessarily define a new type, e.g.:

```python
AgeInt = NewType('AgeInt',int)

def whatIsYourAge(age: AgeInt):
    # do stuff
    return output
```

Other times you want there to be some kind of internal 
consistency, similar to what we did with TypeVar('Any') but
more restrictive -- demanding a specific type.  
You cannot use `TypeVar` here since that is reserved for 
enabling situations that allow for multiple types (e.g., 
`TypeVar('AgeInt',int)` will throw an error). However,
you can use `NewType`:

```python
YearInt = NewType('YearInt', int)

def computeAge(
    currentYear: YearInt,
    birthYear: YearInt,
):
    return currentYear - birthYear
```

### More of my unprocessed notes on NewType
* NewType
  - another way to define new types
  - static type checker will treat the new type as if it 
    were a subclass of the original type
  - e.g., UserId = NewType('UserId', int)
      * to get a type check:  user_a = get_user_name(UserId(42351))
      * you can use UserId(int) wherever you would use int b/c it
        is an int! But it shows more explicit, readable code and
        can be checked with python's type checker
      * note that int operations with UserId types result
        in int types, e.g., `UserId(2) + UserId(3) -> 5` # an int
  - note that defining new types like this is similar to 
    defining a new class, however it is not actually a class;
    these class-like types do not carry any of the overhead
    of a class, but will be treated something like a class
    when using a static type checker; at runtime, there is no
    difference between UserId(5) and just the int 5
  - for similar reasons, one cannot create subtypes of a NewType
    (they are not actually types, so NewType('B',NewType('A'))
    will throw an error)
  - also one cannot base classes on a NewType, e.g.,
    "class MyClass(MyNewType)" will throw an error


# Misc Notes
Misc: 
* Aliases
  - you can technically make an alias for a type, e.g.,
    UserId = int; this helps with readability, but won't throw
    any errors during a static check if int is used instead of
    UserId (for this, see NewType)

* Union   # a way to make hybrid types
* Generic  # another way....
* Generics: # another way to allow for "almost anything"
  - e.g., Mapping, Sequence, TypeVar('T')
  - formerly, one couldn't use "tuple[int,int]" as a type hint;
    similarly for other data structures
  - this was especially true if the type needn't be so specific, 
    e.g., when something can be a tuple or a list
  - so these generics were created, e.g., Sequence[str] means 
    any sequence of strings
* Functions: Callable[[Arg1Type, Arg2Type], ReturnType]


MiscMisc
* iterables in python are types that have __iter__ (they also 
  have a "getitem" like method as the class level that is called
  __class_getitem__)
  - at their most basic form, any iterable is extremely simple
    in that the only requirement is to have __iter__ and there
    is not MRO (it's basically a base type)
  - e.g., see help(collections.abc.Iterable)
* sequences in python types that have __contains__, __getitem__,
  __iter__, __reversed__, count, index, __len__
  - unlike Iterable, this is nowhere near a base type; the MRO
  goes like: Sequence, Reversible, Collection, Sized, Iterable,
  Container, builtins.object
  - see help(collections.abc.Sequence)

* See Also: help() on collections.abc.*
  - e.g., Collection, Container, Mapping, MutableMapping,
    MutableSequence, MutableSet,

Tuple Types:
Defining a Tuple type allows you hint at exactly what type of Tuple
is expected.
e.g., Tuple[str, str, float] lets you specify a specific number of 
elements expected and the type of each position; ellipsis (...) can
be used if the length is non-specific, e.g., Tuple[float,...] for 
a non-specific tuple of floats. 

List Types
The List type automatically implies non-specifity of item count, e.g.,
List[str] means it expects of a list of strings, period.

Advice (from StackOverflow)
For inputs, you likely want to use something more generic than List or
Tuple since a user might use a list or tuple and either likely just as
well internally. The Sequence type allows for this. The more specific
types are more useful when specifying the expected output since this
is something that is more deterministic and you have more control over,
e.g.:  `function(arg: Sequence[str]) -> List[str]`

Advice (mypy docs):  https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
* use Iterable for generic iterables (anything usable in "for")
* use Sequence where a sequence (supporting "len" and "__getitem__") 
  is also required
* use Mapping to describe a dict-like object (with "__getitem__");
  moreover if you are going to use an actual type checker like MyPy,
  then this should be reserved for immutable mapping objects
* use MutableMapping to describe a dict-like object that has both 
  "__getitem__" and "__setitem__", e.g., a dict is technically a 
  mutable mapping whereas an immutable dict would be a dict that
  can't be be mutated after it is initialized (in python, you could 
  say this is a dict that *shouldn't* be mutated after it's 
  initialized, or you could acquire some immutable dict defs and 
  similar data structures from available pythong packages, e.g., 
  examples below).
  - Immutables for Python
      * https://pypi.org/project/immutables/ 
      * https://github.com/MagicStack/immutables
      * https://pypi.org/project/immutabledict/
* use "typing.Match" to describe regex matches from the re module
  - e.g.:  x: Match[str] = re.match(r'[0-9]+', "15")
  
  
Annotated
* LimitedInt = Annotated[int, ValueRange(-10, 5)]
* TwoItemList = Annotated[List[str], 2]
```
T = TypeVar('T')
TupleMax5 = Annotated[Tuple, 'MaxLen(5)']
TwoTuple = tuple[T, T]
TwoTupleVec = List[TwoTuple]
TwoTupleVecMax10 = Annotated[TwoTupleVec, 'MaxLen(10)']
```
* all the example show ValueRange and MaxLen being used, but if 
  I do that I get an error; I've googled it like crazy and all 
  I found is saying something like "those are just examples"; thought
  maybe I needed py39, so I conda installed it and tried: still 
  errors; so...basically you can put it as a string at least...


TypeHints
* typing.get_type_hints


CONTINUE READING:
* https://python.readthedocs.io/en/stable/library/typing.html
