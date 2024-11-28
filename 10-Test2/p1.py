def card_value(card):
    if card in "AJKQT":
        return 10
    else:
        return int(card)
    
def f(player1,player2):
    total1 = sum(card_value(card) for card in player1)
    total2 = sum(card_value(card) for card in player2)
    return total1 >= total2

if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))