from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'C_GenInstructions_1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class BlueInstructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"


class YellowInstructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return "victim" in player.session.config['name']


page_sequence = [BlueInstructions, YellowInstructions]
