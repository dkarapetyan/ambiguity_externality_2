from otree.api import *
import csv
import random
import os

doc = """
a.k.a. Encryption Game
"""


class Constants(BaseConstants):
    data_path = os.path.join("H_EncryptionTask1", "bluematch.csv")
    with open(data_path, encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    players_per_group = None
    name_in_url = "encrypt1"
    num_rounds = 2
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


# PAGES
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


class Hidden(Page):
    timeout_seconds = 0


class Complete(Page):
    pass


class Hidden2(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.externality_I = int(0)
        if player.session.config['name'] == "perp":
            if player.round_number == 1:
                player.blue_ext = random.randint(0, 1)
            if player.round_number == 2:
                player.blue_ext = 1-player.blue_ext
        player.participant.tokens_I = (2 - (player.blue_ext * 0.5)) * player.performance
        player.participant.performance_I = player.performance
        if "victim" in player.session.config['name']:
            matchrow = random.randint(0, (len(Constants.rows) - 1))
            player.participant.bluematch = Constants.rows[matchrow]['participant.code']
            player.participant.externality_I = int(Constants.rows[matchrow]['H_PartI_EncryptionTask.1.player.performance'])
        player.participant.payoff_I = max(player.participant.tokens_I-player.participant.externality_I, 0)


class Results(Page):
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if "victim" in player.session.config['name']:
            return "X_Exit"


page_sequence = [
    BeginEncryptionTask,
    Task,
    Hidden,
    Complete,
    Hidden2,
    Results
]
