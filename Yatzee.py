# import random

# top_half_score = ["", "", "", "", "", ""]
# bottom_half_score = ["", "", "", "", "", "", "", ""]
final_hand = []

bonus = 0

top_half_complete = False
bottom_half_complete = False
human_player = bool
random_generation = bool
game_over = False


# roll #1, generate 5 random d6 rolls and store as working values
# for roll in rolls:
#    current_hand.append(random.randint(1,7))
#    current_hand.sort()
# print(current_hand)
# final_hand = current_hand


def manual_hand():
    temp_hand: list[int] = []
    test_hand_string = input('Please enter 5 numbers, each separated by a comma.\n')
    for i in test_hand_string.split(","):
        int_i = int(i)
        temp_hand.append(int_i)
    temp_hand.sort()
    print(f'\nYour hand is {temp_hand}.\n')
    use_roll_1 = input('\nWould you like to roll any dice?\n')
    if use_roll_1 == "Y":
        temp_hand = []
        test_hand_string = input('\nPlease enter your new hand.\n')
        for i in test_hand_string.split(","):
            int_i = int(i)
            temp_hand.append(int_i)
        temp_hand.sort()
        print(f'\nYour hand after 1 roll is {temp_hand}.\n')
        use_roll_2 = input('Would you like to roll any dice?\n')
        if use_roll_2 == "Y":
            temp_hand = []
            test_hand_string = input("\nPlease enter your new hand.\n")
            for i in test_hand_string.split(","):
                int_i = int(i)
                temp_hand.append(int_i)
            temp_hand.sort()
            print(f"\nYour final hand is {temp_hand}.\n")
            return temp_hand
        else:
            print(f"\nYour final hand is {temp_hand}.\n")
            return temp_hand
    else:
        print(f"\nYour final hand is {temp_hand}.\n")
        return temp_hand


# Top Half
# sum 1s
# def score_1s():
#     score_temp = 0
#     for number in final_hand:
#         if number == 1:
#             score_temp += 1
#     return score_temp


# sum 2s
# def score_2s():
#     score_temp = 0
#     for number in final_hand:
#         if number == 2:
#             score_temp += 2
#     return score_temp


# # sum 3s
# def score_3s():
#     score_temp = 0
#     for number in final_hand:
#         if number == 3:
#             score_temp += 3
#     return score_temp
#
#
# # sum 4s
# def score_4s():
#     score_temp = 0
#     for number in final_hand:
#         if number == 4:
#             score_temp += 4
#     return score_temp
#
#
# # sum 5s
# def score_5s():
#     score_temp = 0
#     for number in final_hand:
#         if number == 5:
#             score_temp += 5
#     return score_temp
#
#
# # sum 6s
# def score_6s():
#     score_temp = 0
#     for number in final_hand:
#         if number == 6:
#             score_temp += 6
#     return score_temp


# Total Top Half
# if sum > 63 get 35 pts
# def score_top_half():
#     temp_score_top_half = 0
#     for entry in top_half_score:
#         temp_score_top_half += entry
#     if temp_score_top_half > 63:
#         temp_score_top_half += 35
#     else:
#         return temp_score_top_half


# Bottom Half
# 3 of a kind = sum of hand if it contains 3 of the same number
# def score_three_of_a_kind():
#     score_temp = 0
#     previous_number = 0
#     n = 0
#     for number in final_hand:
#         if number == previous_number:
#             n += 1
#         else:
#             previous_number = number
#     if n >= 2:
#         for number in final_hand:
#             score_temp += number
#     else:
#         print("This hand can not be scored as a 3 of a kind.")
#     return score_temp
#
#
# # 4 of a kind = sum of hand if it contains 4 of the same number
# def score_four_of_a_kind():
#     score_temp = 0
#     previous_number = 0
#     n = 0
#     for number in final_hand:
#         if number == previous_number:
#             n += 1
#         else:
#             previous_number = number
#     if n >= 3:
#         for number in final_hand:
#             score_temp += number
#     else:
#         print("This hand can not be scored as a 4 of a kind.")
#     return score_temp


# # full house = pair and 3 of a kind
# def score_full_house():
#     score_temp = 0
#     previous_number_1 = 0
#     previous_number_2 = 0
#     n1 = 0
#     n2 = 0
#     for number in final_hand:
#         if previous_number_1 == 0:
#             previous_number_1 = number
#         elif number == previous_number_1:
#             n1 += 1
#         elif previous_number_2 == 0:
#             previous_number_2 = number
#         elif number == previous_number_2:
#             n2 += 1
#         else:
#             previous_number_1 = previous_number_2
#             previous_number_2 = number
#     if n1 >= 2 and n2 >= 3:
#         score_temp = 25
#         return score_temp
#     elif n2 >= 3 and n2 >= 3:
#         score_temp = 25
#         return score_temp
#     else:
#         print("This hand can not be scored as a 4 of a kind.")
#     return score_temp
#
#
# # small straight = 4 in a row ascending
# def score_small_straight():
#     score_temp = 0
#     string_straight = ""
#     previous_number = 0
#     for number in final_hand:
#         if number != previous_number:
#             string_straight += str(number)
#     if "1234" or "2345" or "3456" in string_straight:
#         score_temp = 30
#     else:
#         print("This hand can not be scored as a small straight.")
#     return score_temp
#
#
# # large straight = 5  ascending numbers
# def score_large_straight():
#     score_temp = 0
#     string_straight = ""
#     previous_number = 0
#     for number in final_hand:
#         if number != previous_number:
#             string_straight += str(number)
#     if "12345" or "23456" in string_straight:
#         score_temp = 40
#     else:
#         print("This hand can not be scored as a large straight.")
#     return score_temp
#
#
# # yahtzee, 5 of a kind = 50 pts
# def score_yahtzee():
#     score_temp = 0
#     previous_number = 0
#     n = 0
#     for number in final_hand:
#         if number == previous_number:
#             n += 1
#         else:
#             previous_number = number
#     if n == 4:
#         score_temp = 50
#     else:
#         print("This hand can not be scored as a yahtzee.")
#     return score_temp
#
#
# # chance = sum all dice in hand
# def score_chance():
#     score_temp = 0
#     for number in final_hand:
#         score_temp += number
#     return score_temp
#

def manual_score():
    score_select = input("Please select one of the following scoring "
                         "options.\n1\n2\n3\n4\n5\n6\n3x\n4x\nsm\nlg\nfh\nyz\nch\n\n")
    if (not "1" and not "2" and not "3" and not "4" and not "5"
            and not "6" and not "3x" and not "4x" and not "sm"
            and not "lg" and not "fh" and not "yz" and "ch"
            in score_input):
        manual_score()
    else:
        return score_select


"""
if bonus == 1:
 bottom_half_score[7] = 100
elif bonus == 2:
    bottom_half_score[7] = 200
elif bonus == 3:
    bottom_half_score[7] = 300
"""


# Total Bottom Half
def score_bottom_half():
    temp_score_bottom_half = 0
    for entry in bottom_half_score:
        temp_score_bottom_half += entry
    return temp_score_bottom_half


# Ask for human player, then set preference
# Ask for manual number generation, then set preference
player_input: str = input("Would you like to run this program manually? Y or N\n")
if player_input == "Y":
    human_player = True
    print("\nPlayer has been given control.\n")
else:
    human_player = False
    print("\nComputer has been given control.\n")
# Ask for manual number generation, then set preference
die_input: str = input("Would you like to manually generate the die values? Y or N\n")
if die_input == "Y":
    random_generation = True
    print("\nDice rolls will be manually input.\n")
else:
    random_generation = False
    print("\nDice rolls will be computer generated.\n")


# Human player and manual generation
if human_player and random_generation:
    while not game_over:
        # roll hand and set final hand equal to roll
        final_hand = manual_hand()
        # ask which category to score then score it
        # multiple yahtzee will prompt an additional score round
        # for the top half + 3x, 4x, chance using yahtzee
        print(F"\nTop half: \n{top_half_score}")
        print(F"\nBottom Half: \n{bottom_half_score}\n")
        score_input = manual_score()
        if score_input == '1':
            top_half_score[0] = score_1s()
        elif score_input == '2':
            top_half_score[1] = score_2s()
        elif score_input == '3':
            top_half_score[2] = score_3s()
        elif score_input == '4':
            top_half_score[3] = score_4s()
        elif score_input == '5':
            top_half_score[4] = score_5s()
        elif score_input == '6':
            top_half_score[5] = score_6s()
        elif score_input == '3x':
            bottom_half_score[0] = score_three_of_a_kind()
        elif score_input == '4x':
            bottom_half_score[1] = score_four_of_a_kind()
        elif score_input == 'fh':
            bottom_half_score[2] = score_full_house()
        elif score_input == 'sm':
            bottom_half_score[3] = score_small_straight()
        elif score_input == 'lg':
            bottom_half_score[4] = score_large_straight()
        elif score_input == 'yz':
            if bottom_half_score[5] != 50:
                bottom_half_score[5] = score_yahtzee()
            else:
                bonus += 1
                bottom_half_score[7] = bonus * 100
                score_input = manual_score()
                if score_input == '1':
                    top_half_score[0] = score_1s()
                elif score_input == '2':
                    top_half_score[1] = score_2s()
                elif score_input == '3':
                    top_half_score[2] = score_3s()
                elif score_input == '4':
                    top_half_score[3] = score_4s()
                elif score_input == '5':
                    top_half_score[4] = score_5s()
                elif score_input == '6':
                    top_half_score[5] = score_6s()
                elif score_input == '3x':
                    bottom_half_score[0] = score_three_of_a_kind()
                elif score_input == '4x':
                    bottom_half_score[1] = score_four_of_a_kind()
                elif score_input == 'ch':
                    bottom_half_score[6] = score_chance()
        elif score_input == 'ch':
            bottom_half_score[6] = score_chance()
        print("\n")
        print(top_half_score)
        print("\n")
        print(bottom_half_score)
        print("\n")
        # Check if the top or bottom sections have been filled. Then score the checked section.
        """
        if not top_half_complete:
            for x in top_half_score:
                if isinstance(x, int):
                    top_half_final_score = score_top_half()
                    top_half_complete = True
        if not top_half_complete:
            for x in bottom_half_score:
                if isinstance(x, int):
                    bottom_half_score = score_bottom_half()
                    bottom_half_complete = True
        if top_half_complete and bottom_half_complete:
            game_over = True
            """
