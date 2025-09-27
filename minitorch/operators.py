"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(a: float, b: float):
    return a * b

def id(a: float):
    return a

def add(a: float, b: float):
    return a + b

def neg(a: float):
    return -a

def lt(a: float, b: float):
    return a < b

def eq(a: float, b: float):
    return a == b

def max(a: float, b: float):
    return a if a > b else b

def is_close(a: float, b: float, eps: float = 1e-8):
    return abs(a - b) < eps

def exp(a: float):
    return math.exp(a)

def sigmoid(a: float):
    return 1.0 / (1.0 + math.exp(-a)) if a >=0 else math.exp(a) / (1.0 + math.exp(a))

def relu(a: float):
    return a * (a > 0)

def log(a: float):
    return math.log(a)

def inv(a: float):
    return 1 / a

def log_back(a: float, n: float):
    if a <= 0:
        raise Exception
    return n / a

def inv_back(a: float, n: float):
    return -n / (a**2)

def relu_back(a: float, n: float):
    return n * (a > 0)

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(func: Callable, l: Iterable):
    return [func(el) for el in l]

def zipWith(func: Callable, first: Iterable, second: Iterable):
    return [func(el1, el2) for el1, el2 in zip(first, second)]

def reduce(func: Callable, l: Iterable):
    it = iter(l)
    try:
        acc = next(it)
    except StopIteration:
        raise TypeError("reduce() of empty iterable with no initial value")
    for x in it:
        acc = func(acc, x)
    return acc

def negList(l: Iterable):
    return map(neg, l)

def addLists(a: Iterable, b: Iterable):
    return zipWith(add, a, b)

def sum(l: Iterable):
    try:
        return reduce(add, l)
    except TypeError:
        return 0

def prod(l: Iterable):
    try:
        return reduce(mul, l)
    except TypeError:
        return 1
