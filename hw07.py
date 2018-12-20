import random

count_try = 0
drop_list = []
count_incell = 0


def cards():
    player_list = []
    empty_index_list = []
    gamer_list = []
    check_list = []
    i = 0
    n = 0
    # заполняем карточку
    while n < 3:

        while i < 4:
            true_index = random.randrange(0, 8)
            if true_index in empty_index_list:
                continue
            else:
                empty_index_list.append(true_index)
            i += 1

        i = 0
        while i < 9:
            cell_number = random.randrange(1, 90)
            if cell_number in check_list:
                continue
            else:
                player_list.append(cell_number)
                check_list.append(cell_number)
                player_list_sorted = sorted( player_list )
            i += 1

        for cell in player_list_sorted:
            if player_list_sorted.index(cell) in empty_index_list:
                player_list_sorted[player_list_sorted.index(cell)] = " "

        player_list = []
        empty_index_list = []
        i = 0
        gamer_list.append( player_list_sorted )

        n += 1

    return gamer_list


def dice_hit1(list1, list2, drop_list):
    full_list = [list1] + [list2]
    while True:
        drop = random.randrange( 0, 90 )
        if drop in drop_list:
            True
        else:
            print( "выпал боченок с номером - ", drop )
            drop_list.append( drop )
            break

    for lists in full_list:
        for line in lists:
            if drop in line:
                question = input( "Зачеркнуть цифру? (y/n)" )
                line[line.index( drop )] = "--"
    for lists in full_list:
        count_incell = 0
        for line in lists:
            for cell in line:
                if (cell == " ") or (cell == "--"):
                    count_incell += 1
        if count_incell == 27:
            print( "все цифры зачеркнуты  вы победитель" )
            break
    return list1, list2, count_incell, drop_list


answer = input( "Вы готовы  поиграть (y/n)" )
if answer == "y":

    gamer = cards()
    print( "карточка игрока\n ", "=" * 40, "\n", gamer[0], "\n", gamer[1], "\n", gamer[2], "\n", "=" * 40 )
    computer_card = cards()
    print( "карточка компьютера\n ", "=" * 40, "\n", computer_card[0], "\n", computer_card[1], "\n", computer_card[2],
           "\n", "=" * 40 )

    while (answer != "n") or (count_incell != 10):
        dice_hit1( gamer, computer_card, drop_list )
        count_try += 1
        drop_list = drop_list
        count_incell = count_incell
        print( "карточка игрока\n ", "=" * 40, "\n", gamer[0], "\n", gamer[1], "\n", gamer[2], "\n", "=" * 40 )
        print( "карточка компьютера\n ", "=" * 40, "\n", computer_card[0], "\n", computer_card[1], "\n",
               computer_card[2], "\n", "=" * 40 )
        answer = input( "впереди бросков - %d , продолжать (любая клавиша или n)? -" % (90 - count_try) )
        print( count_incell )
else:
    print( "до свидания" )
