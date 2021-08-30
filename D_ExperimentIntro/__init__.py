from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'D_ExperimentIntro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class BlueIntro(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"

class BlueIntro2(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"

class Yellow1Intro(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] != "perp"

class Yellow2Intro(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] != "perp"

page_sequence = [BlueIntro, BlueIntro2, Yellow1Intro, Yellow2Intro]
