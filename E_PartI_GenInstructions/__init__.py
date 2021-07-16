from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'E_PartI_GenInstructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class GenInstructions(Page):
    pass

class YellowInstructions(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim"

class BlueInstructions(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"

page_sequence = [GenInstructions,YellowInstructions,BlueInstructions]
