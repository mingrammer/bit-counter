# Bit Counter

A simple bit counter. There are 2 types of bit counter: increment and decrement. Bit counter idea was borrowed from digital bit counter. Each index of an array represents each bit of a bit sequence.

## Run & Test

```bash
# 6 bit counter example
python3 main.py

# 8 bit counter tests
python3 test.py
```

## Increment

Increment the bit count by 1. It inverts 1 to 0 until it encounters 0, and inverts 0 to 1 when it encounters 0.

### Increase 7 (000111) to 8 (001000)

```
000111
     ^ (1 to 0)
000110
    ^ (1 to 0)
000100
   ^ (1 to 0)
001000
  ^ (0 to 1)
```

```python
def increment(bits):
    i = 0
    m = len(bits) - 1
    while i <= m and bits[m-i] == 1:
        bits[m-i] = 0
        i += 1
    # Index overflow prevention
    if i <= m:
        bits[m-i] = 1
```

## Decrement

Decrement the bit count by 1. It inverts 0 to 1 until it encounters 1, and inverts 1 to 0 when it encounters 1.

### Decrease 8 (001000) to 7 (000111)

```
001000
     ^ (0 to 1)
001001
    ^ (0 to 1)
001011
   ^ (0 to 1)
000111
  ^ (1 to 0)
```

```python
def decrement(bits):
    i = 0
    m = len(bits) - 1
    while i <= m and bits[m-i] == 0:
        bits[m-i] = 1
        i += 1
    # Index overflow prevention
    if i <= m:
        bits[m-i] = 0
```