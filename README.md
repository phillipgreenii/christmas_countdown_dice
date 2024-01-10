# Overview

We have a dice set which works as a count down timer for christmas.  However, the choice of numbers on the dice don't allow for all days to be represented.  (The set we have only has one dice with '0', so '07' can't be represented).  After working out a solution by hand which works, I was curious to know how many solutions existed.  This code iterates through all possible dice combinations to see how many would work.

# Answer

```
20/9018009
(Die(a=0, b=1, c=2, d=3, e=4, f=5), Die(a=0, b=1, c=2, d=6, e=7, f=8))
(Die(a=0, b=1, c=2, d=3, e=4, f=6), Die(a=0, b=1, c=2, d=5, e=7, f=8))
(Die(a=0, b=1, c=2, d=3, e=4, f=7), Die(a=0, b=1, c=2, d=5, e=6, f=8))
(Die(a=0, b=1, c=2, d=3, e=4, f=8), Die(a=0, b=1, c=2, d=5, e=6, f=7))
(Die(a=0, b=1, c=2, d=3, e=5, f=6), Die(a=0, b=1, c=2, d=4, e=7, f=8))
(Die(a=0, b=1, c=2, d=3, e=5, f=7), Die(a=0, b=1, c=2, d=4, e=6, f=8))
(Die(a=0, b=1, c=2, d=3, e=5, f=8), Die(a=0, b=1, c=2, d=4, e=6, f=7))
(Die(a=0, b=1, c=2, d=3, e=6, f=7), Die(a=0, b=1, c=2, d=4, e=5, f=8))
(Die(a=0, b=1, c=2, d=3, e=6, f=8), Die(a=0, b=1, c=2, d=4, e=5, f=7))
(Die(a=0, b=1, c=2, d=3, e=7, f=8), Die(a=0, b=1, c=2, d=4, e=5, f=6))
(Die(a=0, b=1, c=2, d=4, e=5, f=6), Die(a=0, b=1, c=2, d=3, e=7, f=8))
(Die(a=0, b=1, c=2, d=4, e=5, f=7), Die(a=0, b=1, c=2, d=3, e=6, f=8))
(Die(a=0, b=1, c=2, d=4, e=5, f=8), Die(a=0, b=1, c=2, d=3, e=6, f=7))
(Die(a=0, b=1, c=2, d=4, e=6, f=7), Die(a=0, b=1, c=2, d=3, e=5, f=8))
(Die(a=0, b=1, c=2, d=4, e=6, f=8), Die(a=0, b=1, c=2, d=3, e=5, f=7))
(Die(a=0, b=1, c=2, d=4, e=7, f=8), Die(a=0, b=1, c=2, d=3, e=5, f=6))
(Die(a=0, b=1, c=2, d=5, e=6, f=7), Die(a=0, b=1, c=2, d=3, e=4, f=8))
(Die(a=0, b=1, c=2, d=5, e=6, f=8), Die(a=0, b=1, c=2, d=3, e=4, f=7))
(Die(a=0, b=1, c=2, d=5, e=7, f=8), Die(a=0, b=1, c=2, d=3, e=4, f=6))
(Die(a=0, b=1, c=2, d=6, e=7, f=8), Die(a=0, b=1, c=2, d=3, e=4, f=5))
```

# Run
```bash
./run.sh
```

# Develpoment
```bash
nix-shell
```
