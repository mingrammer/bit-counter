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

```
00000000
00000001
00000010
00000011
00000100
........
```

### How it works

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

### Implementation

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

```
11111111
11111110
11111101
11111100
11111011
........
```

### How it works

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

### Implementation

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
