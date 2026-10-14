import random

orel = "orel"
reshka = "reshka"
cn = [orel, reshka]

def flip():
    return random.choice(cn)

def martingale(*, depozit: int, min_bet: int, max_bet: int) -> tuple[int, int]:
    steps = 0
    #current_bet = min_bet
    max_depozit = depozit
    while depozit > 0:
       # current_bet = min(current_bet, depozit)
        steps += 1
        depozit -= min_bet   #current_bet
        flipping_coin = random.choice(cn)
        print("=====")
        print(f"Ставка: {min_bet}")  #current_bet
        print(f"Выпало: {flipping_coin}")
        if flipping_coin == random.choice(cn):
            win = min_bet * 2   #current_bet
            depozit += win
            print(f"Выигрыш: {win}")
           # current_bet = min_bet
        else:
            print("Проигрыш")
            min_bet *= 2            # current_bet
            if min_bet > max_bet:     # current_bet
                min_bet = max_bet       # current_bet
        if depozit > max_depozit:
            max_depozit = depozit
        print(f"Текущий депозит: {depozit}")
    return steps, max_depozit

steps, max_depozit = martingale(depozit=100, min_bet=1, max_bet=100)

print("---==============---")
print(f"Колво раундов: {steps}")
print(f"Максимальный деп: {max_depozit}")