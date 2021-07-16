from otree.api import *
import csv
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'I_PartI_RevealEarnings'
    players_per_group = None
    num_rounds = 1
    with open('I_partI_RevealEarnings/bluematch.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES


class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        #the variable name at the end of the next line might change when we run it properly with a "H_" prefix
        player.participant.externality_I = int(0)
        if player.session.config['name'] == "victim":
            player.participant.externality_I = int(Constants.rows[random.randint(0, (len(Constants.rows)-1))]['H_PartI_EncryptionTask.1.player.performance'])
        player.participant.payoff_I = max(player.participant.tokens_I-player.participant.externality_I, 0)


class Results(Page):
    pass


page_sequence = [Hidden, Results]
