from typing import NamedTuple, List, Iterator, Set, Dict, Tuple

class Die(NamedTuple):
    a:int
    b:int
    c:int
    d:int
    e:int
    f:int

Dice = Tuple[Die,Die]

Day = Tuple[int,int]

class Score(NamedTuple):
    possible:Tuple[int,...]
    all_possible:bool

def generate_christmas_dates()->Iterator[Day]:
    for n in range(24+1):
        d1 = n//10
        d0 = n%10
        if d1 == 9 or d0 == 9:
            # skipping 9s because 6 can be flipped upside down
            continue
        yield (d1,d0)

def generate_test_dates()->Iterator[Day]:
    for n in range(3+1):
        d1 = n//10
        d0 = n%10
        if d1 == 9 or d0 == 9:
            # skipping 9s because 6 can be flipped upside down
            continue
        yield (d1,d0)

def generate_die()->Iterator[Die]:
    ds = [0,1,2,3,4,5,6,7,8]
    # ds = [0,1,2,3]

    for a in range(0,len(ds)):
        for b in range(a,len(ds)):
            for c in range(b,len(ds)):
                for d in range(c,len(ds)):
                    for e in range(d,len(ds)):
                        for f in range(e,len(ds)):
                            yield Die(a,b,c,d,e,f)

    # for d in [0,1,2,3,4,5,6,7,8]:
    #     yield d

def generate_dice()->Iterator[Dice]:
    for d1 in generate_die():
        for d2 in generate_die():
            yield (d1,d2)

def can_dice_do_day(dice:Dice,date:Day)->bool:
    # print(dice)
    # print(date)
    return (date[0] in dice[0] and date[1] in dice[1]) or \
        (date[1] in dice[0] and date[0] in dice[1])

def score_dice(dates:List[Day], dice:Dice)->Score:
    possible = [can_dice_do_day(dice,d) for d in dates]
    return Score(tuple(possible),all(possible))

def test_can_dice_do_day():
    date = (0,2)
    dice = (Die(0,1,2,3,4,5),Die(0,1,2,3,4,5))

    print(can_dice_do_day(dice,date))

def test_score_dice():
    dates = [(0,0),(0,1),(0,2)]
    dice = (Die(0,1,2,3,4,5),Die(0,1,2,3,4,5))
    print(score_dice(dates,dice))

# test_can_dice_do_day()
# test_score_dice()

def main(): 
    print("Generating Christmas Dates")
    christmas_dates = list(generate_christmas_dates())
    # christmas_dates = list(generate_test_dates())
    # print(christmas_dates)
    works = {}
    count = 0
    print("Generating Dice Compinations")
    for dice in generate_dice():
        score = score_dice(christmas_dates, dice)
        count += 1
        if score.all_possible:
            works[dice] = score
        # print(score)
        # break

    print(f"Found {len(works)}/{count}")
    for w in works.keys():
        print(w)
        

if __name__ == '__main__':
    main()

