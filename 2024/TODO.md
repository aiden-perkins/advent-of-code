- clean up day 12
- betterer for 9 and 14
- remove to_move in day 15

```python
# this is day 17 p2
target = '2417750340175530'
actual_a = [0]

for v in target[::-1]:
    possible_as = []
    for paa in actual_a:
        paa *= 8
        possible_answers = []
        for a in range(8):
            ta = paa + a
            tb = a ^ 7
            tc = ta // (2 ** tb)
            tb ^= tc
            tb ^= 7
            tb %= 8
            if tb == int(v):
                possible_answers.append(a)
        for cva in possible_answers:
            possible_as.append(paa + cva)
    actual_a = possible_as

print(min(actual_a))
```
