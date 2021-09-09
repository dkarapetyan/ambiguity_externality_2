from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'I_GenInstructions_2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class BlueInstructions_2(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"


page_sequence = [BlueInstructions_2]
