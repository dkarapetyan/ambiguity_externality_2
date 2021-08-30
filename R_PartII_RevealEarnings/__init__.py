from otree.api import *
import csv
import random
import os

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'R_PartII_RevealEarnings'
    data_path = os.path.join("R_PartII_RevealEarnings", "bluematch.csv")
    players_per_group = None
    num_rounds = 1
    with open(data_path, encoding='utf-8') as file:
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
        player.participant.externality_II = int(0)
        if player.session.config['name'] == "victim2":
            matchrow = random.randint(0, (len(Constants.rows)-1))
            player.participant.bluematch = Constants.rows[matchrow]['participant.code']
            player.participant.ext_choice = int(Constants.rows[matchrow]['R_PartII_EncryptionTask.1.player.externality'])
            player.participant.externality_II = (2-player.participant.ext_choice)*(int(Constants.rows[matchrow]['R_PartII_EncryptionTask.1.player.performance']))
            player.participant.payoff_II = max(player.participant.tokens_II-player.participant.externality_II, 0)
        else:
            if player.participant.externality_II == 2:
                player.participant.payoff_II = player.participant.tokens_II*0.75


class Results(Page):
    pass


page_sequence = [Hidden, Results]
