num_card = []
card_desk = []
for i in range(13):
    if i == 0:
        num_card.append('Tuz')
    elif i == 1:
        num_card.append('Korol')
    elif i == 11:
        num_card.append('Valet')
    elif i == 12:
        num_card.append('Dama')
    else:
        num_card.append(i)
for y in num_card:
    card_desk.append(str(y) + ' Piki')
    card_desk.append(str(y) + ' Krest')
    card_desk.append(str(y) + ' Cherva')
    card_desk.append(str(y) + ' Buba')

print(num_card)
print(card_desk)
iter_card_desk = iter(card_desk)
while True:
    try:
        i = next(iter_card_desk)
        print(i)
    except StopIteration:
        break
