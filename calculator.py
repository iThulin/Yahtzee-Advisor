import random


class Calculator:
    def __init__(self):
        self.hand_list = [0, 0, 0, 0, 0]
        self.top_half_score = ["", "", "", "", "", ""]
        self.bottom_half_score = ["", "", "", "", "", "", "", ""]
        self.score_temp = 0
        self.top_half_score_temp = 0
        self.top_half_total = 0
        self.top_half_bonus = self.top_half_total - 63
        self.bottom_half_total = 0
        self.working_number = 0
        self.working_number_2 = 0
        self.matches = 0
        self.matches_2 = 0
        self.string_straight = ""
        self.rolls_remaining = 3
        self.turns_remaining = int

    # Search the hand_list and reroll all dice that have been marked 
    # (negative value or 0),
    #  then adjust rolls remaining variable
    def roll_marked_dice(self):
        for index, die in enumerate(self.hand_list):
            if die <= 0:
                self.hand_list[index] = random.randint(1, 6)
        self.rolls_remaining -= 1

    # Set temp numbers to 0
    def reset_temp_variables(self):
        self.score_temp = 0
        self.top_half_score_temp = 0
        self.working_number = 0
        self.working_number_2 = 0
        self.matches = 0
        self.matches_2 = 0
        self.string_straight = ""
        self.turns_remaining = 0

    # Sum the value of all instances of a particular number in the hand,
    # then set self.score_temp equal to the sum of the number.
    def calculate_1s(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == 1:
                self.score_temp += 1

    def calculate_2s(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == 2:
                self.score_temp += 2

    def calculate_3s(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == 3:
                self.score_temp += 3

    def calculate_4s(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == 4:
                self.score_temp += 4

    def calculate_5s(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == 5:
                self.score_temp += 5

    def calculate_6s(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == 6:
                self.score_temp += 6

    # Sum all entries in the top half list.
    # If the total is > 63 then enable the top half bonus.
    def calculate_top_half(self):
        self.reset_temp_variables()
        for entry in self.top_half_score:
            self.top_half_score_temp += entry
        if self.top_half_score_temp > 35:
            self.top_half_bonus = True

    # Determine if the hand contains 3 of the same number.
    # # If this can be scored self.score_temp is set to the sum of all numbers 
    # in the hand.
    def calculate_3_of_a_kind(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == self.working_number:
                self.matches += 1
            else:
                self.working_number = number
        if self.matches >= 2:
            for number in self.hand_list:
                self.score_temp += number

    # Determine if the hand contains 4 of the same number.
    # If this can be scored self.score_temp is set to the sum of all numbers in 
    # the hand.
    def calculate_4_of_a_kind(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == self.working_number:
                self.matches += 1
            else:
                self.working_number = number
        if self.matches >= 3:
            for number in self.hand_list:
                self.score_temp += number

    # Determine if the hand has a pair and 3 of a kind.
    # If this can be scored self.score_temp is set to 25 pts.
    def calculate_full_house(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == self.working_number:
                self.matches += 1
            elif number == self.working_number_2:
                self.matches_2 += 1
            else:
                self.working_number = self.working_number_2
                self.working_number_2 = number
        if self.matches >= 2 and self.matches_2 >= 3:
            self.score_temp = 25
        elif self.matches >= 3 and self.matches_2 >= 2:
            self.score_temp = 25
        else:
            self.score_temp = 0

    # Determine if the hand has 4 numbers ascending in a row.
    # If this can be scored self.score_temp is set to 25 pts.
    def calculate_small_straight(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number != self.working_number:
                self.string_straight += str(number)
        if "1234" or "2345" or "3456" in self.string_straight:
            self.score_temp = 30

    # Determine if the hand has 5 numbers ascending in a row.
    # If this can be scored self.score_temp is set to 40 pts.
    def calculate_large_straight(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number != self.working_number:
                self.string_straight += str(number)
        if "12345" or "23456" in self.string_straight:
            self.score_temp = 40

    # Determine if the hand has 5 identical 5.
    # If this can be scored self.score_temp is set to 50 pts.
    def calculate_yatzee(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            if number == self.working_number:
                self.matches += 1
            else:
                self.working_number = number
        if self.matches == 4:
            self.score_temp = 50

    # Sum of all dice in hand, set self.score_temp to the total, and decrement
    # the turns remaining counter.
    def calculate_chance(self):
        self.reset_temp_variables()
        for number in self.hand_list:
            self.score_temp += number

    # Checks which categories have been scored for the top and bottom half 
    # score, then returns an int for how many turn remain for the player.
    def calculate_turns_remaining(self):
        self.reset_temp_variables()
        for number in self.top_half_score:
            if number == "":
                self.turns_remaining += 1
        for number in self.bottom_half_score:
            if number == "":
                self.turns_remaining += 1

