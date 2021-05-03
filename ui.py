from tkinter import *
from calculator import Calculator
import random

THEME_COLOR = "#323031"
HEADER_COLOR = "#589094"
TEXT_COLOR = "#969d99"
SCORE_COLOR = "#be9b6a"
HEADER = ("arial", 30, "bold")
BODY = ("Arial", 15, "bold")


class AdvisorInterface:
    def __init__(self, calculator: Calculator):
        self.scores = calculator
        self.top_half_scores = calculator.top_half_score
        self.top_half_total = calculator.top_half_total
        self.bottom_half_total = calculator.bottom_half_total
        self.bottom_half_scores = calculator.bottom_half_score
        self.rolls_remaining = calculator.rolls_remaining
        self.hand_list = calculator.hand_list

        # Set up Main Window
        self.window = Tk()
        self.window.title("Yahtzee Advisor")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(height=1000, width=1000, bg="White")

        # Create Die Images
        self.photo_0 = PhotoImage(file="images/120px-Dice-0.png")
        self.photo_1 = PhotoImage(file="images/120px-Dice-1-b.png")
        self.photo_2 = PhotoImage(file="images/120px-Dice-2-b.png")
        self.photo_3 = PhotoImage(file="images/120px-Dice-3-b.png")
        self.photo_4 = PhotoImage(file="images/120px-Dice-4-b.png")
        self.photo_5 = PhotoImage(file="images/120px-Dice-5-b.png")
        self.photo_6 = PhotoImage(file="images/120px-Dice-6-b.png")

        # Create Reroll Images
        self.photo_reroll_1 = PhotoImage(file="images/120px-Dice-1.png")
        self.photo_reroll_2 = PhotoImage(file="images/120px-Dice-2.png")
        self.photo_reroll_3 = PhotoImage(file="images/120px-Dice-3.png")
        self.photo_reroll_4 = PhotoImage(file="images/120px-Dice-4.png")
        self.photo_reroll_5 = PhotoImage(file="images/120px-Dice-5.png")
        self.photo_reroll_6 = PhotoImage(file="images/120px-Dice-6.png")

        # Upper Section labels and Scores Table
        self.top_half_label = Label(text="Upper Section", font=HEADER, bg=THEME_COLOR, fg=HEADER_COLOR)
        self.top_half_label.grid(row=0, column=0, columnspan=2, pady=[0, 20])

        self.aces_label = Label(text="Aces ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.aces_label.grid(row=1, column=0, sticky="E")
        self.aces_score = Label(text=f"{self.top_half_scores[0]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.aces_score.grid(row=1, column=1, sticky="W")

        self.twos_label = Label(text="Twos ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.twos_label.grid(row=2, column=0, sticky="E")
        self.twos_score = Label(text=f"{self.top_half_scores[1]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.twos_score.grid(row=2, column=1, sticky="W")

        self.threes_label = Label(text="Threes ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.threes_label.grid(row=3, column=0, sticky="E")
        self.threes_score = Label(text=f"{self.top_half_scores[2]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.threes_score.grid(row=3, column=1, sticky="W")

        self.fours_label = Label(text="Fours ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.fours_label.grid(row=4, column=0, sticky="E")
        self.fours_score = Label(text=f"{self.top_half_scores[3]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.fours_score.grid(row=4, column=1, sticky="W")

        self.fives_label = Label(text="Fives ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.fives_label.grid(row=5, column=0, sticky="E")
        self.fives_score = Label(text=f"{self.top_half_scores[4]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.fives_score.grid(row=5, column=1, sticky="W")

        self.sixes_label = Label(text="Sixes ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.sixes_label.grid(row=6, column=0, sticky="E")
        self.sixes_score = Label(text=f"{self.top_half_scores[5]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.sixes_score.grid(row=6, column=1, sticky="W")

        self.bonus_label = Label(text="Bonus ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.bonus_label.grid(row=7, column=0, sticky="E")
        self.bonus_score = Label(text=f"{calculator.top_half_bonus}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.bonus_score.grid(row=7, column=1, sticky="W")

        self.top_total_label = Label(text="Total ", font=BODY, bg=THEME_COLOR, fg=HEADER_COLOR)
        self.top_total_label.grid(row=8, column=0, sticky="E")
        self.top_total_score = Label(text=f"{calculator.top_half_total}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.top_total_score.grid(row=8, column=1, sticky="W")

        # Lower Section Labels and Scores Table
        self.top_half_label = Label(text="Lower Section ", font=HEADER, bg=THEME_COLOR, fg=HEADER_COLOR)
        self.top_half_label.grid(row=0, column=3, columnspan=2, pady=[0, 20])

        self.three_x_label = Label(text="Three of a Kind ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.three_x_label.grid(row=1, column=3, sticky="E")
        self.sixes_score = Label(text=f"{self.bottom_half_scores[0]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.sixes_score.grid(row=1, column=4, sticky="W")

        self.four_x_label = Label(text="Four of a Kind ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.four_x_label.grid(row=2, column=3, sticky="E")
        self.four_x_score = Label(text=f"{self.bottom_half_scores[1]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.four_x_score.grid(row=2, column=4, sticky="W")

        self.full_house_label = Label(text="Full House ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.full_house_label.grid(row=3, column=3, sticky="E")
        self.full_house_score = Label(text=f"{self.bottom_half_scores[2]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.full_house_score.grid(row=3, column=4, sticky="W")

        self.small_straight_label = Label(text="Small Straight ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.small_straight_label.grid(row=4, column=3, sticky="E")
        self.small_straight_score = Label(text=f"{self.bottom_half_scores[3]}", font=BODY, bg=THEME_COLOR,
                                          fg=SCORE_COLOR)
        self.small_straight_score.grid(row=4, column=4, sticky="W")

        self.large_straight_label = Label(text="Large Straight ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.large_straight_label.grid(row=5, column=3, sticky="E")
        self.large_straight_score = Label(text=f"{self.bottom_half_scores[4]}", font=BODY, bg=THEME_COLOR,
                                          fg=SCORE_COLOR)
        self.large_straight_score.grid(row=5, column=4, sticky="W")

        self.yahtzee_label = Label(text="Yahtzee ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.yahtzee_label.grid(row=6, column=3, sticky="E")
        self.yahtzee_score = Label(text=f"{self.bottom_half_scores[5]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.yahtzee_score.grid(row=6, column=4, sticky="W")

        self.chance_label = Label(text="Chance ", font=BODY, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.chance_label.grid(row=7, column=3, sticky="E")
        self.chance_score = Label(text=f"{self.bottom_half_scores[6]}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.chance_score.grid(row=7, column=4, sticky="W")

        self.bottom_total_label = Label(text="Total ", font=BODY, bg=THEME_COLOR, fg=HEADER_COLOR)
        self.bottom_total_label.grid(row=8, column=3, sticky="E")
        self.bottom_total_score = Label(text=f"{self.bottom_half_total}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.bottom_total_score.grid(row=8, column=4, sticky="W")

        # Grand Total
        self.grand_total_label = Label(text="Grand Total", font=HEADER, bg=THEME_COLOR, fg=HEADER_COLOR)
        self.grand_total_label.grid(row=8, column=2)
        self.grand_total_score = Label(text=f"{self.bottom_half_total}", font=HEADER, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.grand_total_score.grid(row=9, column=2)

        # Create Die Image Buttons
        self.die_1_image = Button(image=self.photo_0,
                                  highlightthickness=0,
                                  bd=0,
                                  bg=THEME_COLOR,
                                  activebackground=THEME_COLOR,
                                  command=self.mark_d1)
        self.die_1_image.grid(row=12, column=0, pady=50)

        self.die_2_image = Button(image=self.photo_0,
                                  highlightthickness=0,
                                  bd=0,
                                  bg=THEME_COLOR,
                                  activebackground=THEME_COLOR,
                                  command=self.mark_d2)
        self.die_2_image.grid(row=12, column=1, padx=[30, 0], pady=50)

        self.die_3_image = Button(image=self.photo_0,
                                  highlightthickness=0,
                                  bd=0,
                                  bg=THEME_COLOR,
                                  activebackground=THEME_COLOR,
                                  command=self.mark_d3)
        self.die_3_image.grid(row=12, column=2, pady=50)

        self.die_4_image = Button(image=self.photo_0,
                                  highlightthickness=0,
                                  bd=0,
                                  bg=THEME_COLOR,
                                  activebackground=THEME_COLOR,
                                  command=self.mark_d4)
        self.die_4_image.grid(row=12, column=3, padx=[0, 50], pady=50)

        self.die_5_image = Button(image=self.photo_0,
                                  highlightthickness=0,
                                  bd=0,
                                  bg=THEME_COLOR,
                                  activebackground=THEME_COLOR,
                                  command=self.mark_d5)
        self.die_5_image.grid(row=12, column=4, pady=50)

        # Create Advisor info panels
        self.rolls_remaining_label = Label(text=f"Rolls Remaining:", font=BODY, bg=THEME_COLOR, fg=HEADER_COLOR)
        self.rolls_remaining_label.grid(row=14, column=0, sticky="W")
        self.rolls_remaining_number = Label(text=f"{self.rolls_remaining}", font=BODY, bg=THEME_COLOR,
                                            fg=SCORE_COLOR)
        self.rolls_remaining_number.grid(row=14, column=1, sticky="W")

        self.strategy_label = Label(text=f"Current Strategy:", font=BODY, bg=THEME_COLOR, fg=HEADER_COLOR)
        self.strategy_label.grid(row=15, column=0, sticky="W")
        self.strategy_string = Label(text=f"{self.rolls_remaining}", font=BODY, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.strategy_string.grid(row=15, column=1, sticky="W")

        self.roll_dice_button = Button(text="Roll the Dice",
                                       font=BODY,
                                       highlightthickness=0,
                                       bd=0,
                                       bg=HEADER_COLOR,
                                       fg=SCORE_COLOR,
                                       activebackground=THEME_COLOR,
                                       command=self.roll_marked_dice)
        self.roll_dice_button.grid(row=14, column=2)

        self.window.mainloop()

    # Updates the rolls remaining, current strategy and die images
    def update_dice(self):
        self.rolls_remaining_number.config(text=f"{self.rolls_remaining}")
        for index, die in enumerate(self.hand_list):
            if die == - 6:
                if index == 0:
                    self.die_1_image.config(image=self.photo_reroll_6)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_reroll_6)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_reroll_6)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_reroll_6)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_reroll_6)
            elif die == -5:
                if index == 0:
                    self.die_1_image.config(image=self.photo_reroll_5)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_reroll_5)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_reroll_5)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_reroll_5)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_reroll_5)
            elif die == -4:
                if index == 0:
                    self.die_1_image.config(image=self.photo_reroll_4)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_reroll_4)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_reroll_4)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_reroll_4)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_reroll_4)
            elif die == -3:
                if index == 0:
                    self.die_1_image.config(image=self.photo_reroll_3)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_reroll_3)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_reroll_3)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_reroll_3)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_reroll_3)
            elif die == -2:
                if index == 0:
                    self.die_1_image.config(image=self.photo_reroll_2)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_reroll_2)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_reroll_2)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_reroll_2)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_reroll_2)
            elif die == -1:
                if index == 0:
                    self.die_1_image.config(image=self.photo_reroll_1)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_reroll_1)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_reroll_1)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_reroll_1)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_reroll_1)
            elif die == 0:
                if index == 0:
                    self.die_1_image.config(image=self.photo_0)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_0)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_0)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_0)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_0)
            elif die == 1:
                if index == 0:
                    self.die_1_image.config(image=self.photo_1)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_1)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_1)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_1)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_1)
            elif die == 2:
                if index == 0:
                    self.die_1_image.config(image=self.photo_2)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_2)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_2)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_2)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_2)
            elif die == 3:
                if index == 0:
                    self.die_1_image.config(image=self.photo_3)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_3)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_3)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_3)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_3)
            elif die == 4:
                if index == 0:
                    self.die_1_image.config(image=self.photo_4)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_4)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_4)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_4)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_4)
            elif die == 5:
                if index == 0:
                    self.die_1_image.config(image=self.photo_5)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_5)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_5)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_5)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_5)
            elif die == 6:
                if index == 0:
                    self.die_1_image.config(image=self.photo_6)
                elif index == 1:
                    self.die_2_image.config(image=self.photo_6)
                elif index == 2:
                    self.die_3_image.config(image=self.photo_6)
                elif index == 3:
                    self.die_4_image.config(image=self.photo_6)
                elif index == 4:
                    self.die_5_image.config(image=self.photo_6)

    def mark_d1(self):
        if self.hand_list[0] != 0:
            self.hand_list[0] *= -1
            self.update_dice()

    def mark_d2(self):
        if self.hand_list[1] != 0:
            self.hand_list[1] *= -1
            self.update_dice()

    def mark_d3(self):
        if self.hand_list[2] != 0:
            self.hand_list[2] *= -1
            self.update_dice()

    def mark_d4(self):
        if self.hand_list[3] != 0:
            self.hand_list[3] *= -1
            self.update_dice()

    def mark_d5(self):
        if self.hand_list[4] != 0:
            self.hand_list[4] *= -1
            self.update_dice()

    # Search the hand_list and reroll all dice that have been marked (negative value or 0) then adjust rolls
    # remaining variable
    def roll_marked_dice(self):
        for index, die in enumerate(self.hand_list):
            if die <= 0:
                self.hand_list[index] = random.randint(1, 6)
        self.rolls_remaining -= 1
        self.hand_list.sort()
        self.update_dice()
        if self.rolls_remaining == 0:
            self.roll_dice_button.config(state=DISABLED)
            self.die_1_image.config(state=DISABLED)
            self.die_2_image.config(state=DISABLED)
            self.die_3_image.config(state=DISABLED)
            self.die_4_image.config(state=DISABLED)
            self.die_5_image.config(state=DISABLED)
        print(self.hand_list)

    # Scores had based on current strategy, resets hand and rolls remaining to initial state, activates the dice buttons
    def score_current_hand(self):
        self.rolls_remaining = 3
        self.hand_list = [0, 0, 0, 0, 0]
        self.roll_dice_button.config(state=ACTIVE)
        self.die_1_image.config(state=ACTIVE)
        self.die_2_image.config(state=ACTIVE)
        self.die_3_image.config(state=ACTIVE)
        self.die_4_image.config(state=ACTIVE)
        self.die_5_image.config(state=ACTIVE)
