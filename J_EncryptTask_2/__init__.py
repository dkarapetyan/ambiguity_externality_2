from otree.api import *
import csv
import random
import os

doc = """
Encryption Game 2
"""


class Constants(BaseConstants):
    players_per_group = None
    name_in_url = "encrypt2"
    num_rounds = 1
    letters_per_word = 5
    use_timeout = True
    seconds_per_period = 360


class Subsession(BaseSubsession):
    dictionary = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    performance = models.FloatField(initial=0)
    mistakes = models.IntegerField(initial=0)
    bonus = models.IntegerField(initial=0)
    earnings = models.CurrencyField(initial=0)
    bonus_question = models.CurrencyField(initial=0)
    final = models.CurrencyField(initial=0)
    tokens = models.FloatField(initial=0)
    blue_ext = models.IntegerField(initial=0)
    externality = models.IntegerField(initial=0)
    initial_ans = models.StringField(initial="")
    num_wrong = models.IntegerField(initial=0)

    # Perpetrator with externality
    p2_q1 = models.IntegerField(
        label="If you choose to earn 1.5 tokens per word encrypted correctly, how many tokens will your "
              "matched Yellow player lose? ",
        choices=[[1, "1"], [2, "2"], [3, "0"]],
        widget=widgets.RadioSelect
    )
    p2_q2 = models.IntegerField(
        label="If you choose to earn 2 tokens per word encrypted correctly, how many tokens will "
              "your matched Yellow player lose? ",
        choices=[[1, "1"], [2, "2"], [3, "0"]],
        widget=widgets.RadioSelect
    )
    p2_q3 = models.IntegerField(
        label="Your earnings will be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    p2_q4 = models.IntegerField(
        label="You will be paired with the same Yellow player you were paired with in the previous Encryption task.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    ext_choice = models.IntegerField(
        label="Please choose between the two following types of payoffs:",
        choices=[[0, "I would like to earn 2 tokens for every word I encrypt correctly, with a 1 token decrease "
                     "from the earnings of the Yellow player I am paired with."],
                 [1, "I would like to earn 1.5 tokens for every word I encrypt correctly, without decreasing the "
                     "earnings of the Yellow player I am paired with."]],
        widget=widgets.RadioSelect
    )


# PAGES
class EarningsInstructions_p2(Page):
    form_model = "player"
    form_fields = ["p2_q1", "p2_q2", "p2_q3", "p2_q4"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(p2_q1=3, p2_q2=1, p2_q3=1, p2_q4=2,)
        error_messages = dict()

        for field_name in solutions:
            if len(player.initial_ans) < 6:
                player.initial_ans += str(values[field_name])
            if values[field_name] != solutions[field_name]:
                player.num_wrong += 1
                error_messages[field_name] = 'Wrong answer. Click "Back" to review the instructions and try again'

        return error_messages


class ExtChoice(Page):
    form_model = "player"
    form_fields = ["ext_choice"]


class BeginEncryptionTask(Page):
    pass


class Task(Page):
    form_model = "player"
    form_fields = ["performance", "mistakes"]
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {
            "legend_list": legend_list,
            "task_list": task_list,
            "task_width": task_width,
        }


class Complete(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.performance3 = player.performance
        player.tokens = (2 - (player.ext_choice * 0.5)) * player.performance
        player.participant.payoff_choice = player.tokens


class Earnings(Page):
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.session.config['name'] == 'perp':
            return "N_Survey"


page_sequence = [
    EarningsInstructions_p2,
    ExtChoice,
    BeginEncryptionTask,
    Task,
    Complete,
    Earnings
]
