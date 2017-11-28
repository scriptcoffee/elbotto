from elbotto.bots.training.card_parser import create_card
from elbotto.bots.training.trumpf_converter import trumpf_converter


def get_trumpf(round):
    if 'trump' not in round:
        # print("Round hasn't a trump, so we skip it")
        return None
    else:
        trumpf = round['trump']
        return trumpf_converter(trumpf)


def get_remaining_hand_cards(end_hand_list, amount_players, table):
    for player in range(amount_players):
        if 'hand' not in end_hand_list[player]:
            # print("Round has no hands, so we skip it")
            break
        dealer_gift = end_hand_list[player]['hand']
        player_cards = []
        for c in dealer_gift:
            player_cards.append(create_card(c))
        table.insert(player, player_cards)
    return table


def complete_hand_cards_with_stiches(stich_list, amount_players, table):
    amount_stich = len(stich_list)
    if amount_stich == 0:
        # print("No stich exist!")
        return 0
    for stich in range(amount_stich):
        current_player = int(stich_list[stich]['first'])
        for player_seat in range(amount_players):
            played_card = stich_list[stich]['cards'][player_seat]
            card = create_card(played_card)
            table[current_player].append(card)
            current_player = (current_player - 1) % amount_players
    return table


def print_trumpf(game_type):
    if game_type.mode == "TRUMPF":
        print("trumpf: {}".format(game_type.trumpf_color.name))
    else:
        print("trumpf: {}".format(game_type.mode))


def print_table(table):
    print("player0: {}".format(table[0]))
    print("player1: {}".format(table[1]))
    print("player2: {}".format(table[2]))
    print("player3: {}".format(table[3]))