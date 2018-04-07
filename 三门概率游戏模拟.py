import random
import time
import sys

victory = 0
gamenumber = 0
ans = 0


def simulink(change_door):
    global victory, gamenumber, ans

    def judge_man(mans_guess, change_door):
        global ans, victory, gamenumber

        if change_door:
            empty = random.choice(
                list(set([1, 2, 3]) - set([ans, mans_guess])))
            mans_guess = list(set([1, 2, 3]) - (set([mans_guess, empty])))[0]
        else:
            pass

        gamenumber += 1
        if mans_guess == ans:
            victory += 1
            print('>>正确', victory, gamenumber, ' ', victory/gamenumber, end='\r')
        else:
            print('>>错误', victory, gamenumber, ' ', victory/gamenumber, end='\r')
        sys.stdout.flush()

    def guess_man():
        return random.randint(1, 3)

    victory = 0
    gamenumber = 0
    for _ in range(3000):
        # game start
  
        ans = random.randint(1, 3)
        guess = guess_man()

        judge_man(guess, change_door)
        # time.sleep(0.00001)
    print(''*200)
    sys.stdout.flush()
    return '\r[统计]:{0}/{1}\t {2}'.format(victory, gamenumber, victory/gamenumber)


huan = simulink(True)
print()
buhuan = simulink(False)
print('')


_ = input('')
