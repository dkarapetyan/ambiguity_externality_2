from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'M_PartI_Fairness'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    fairness = models.IntegerField(
        choices = [
        [-2, 'Very unfair'],
        [-1, 'Somewhat unfair'],
        [0, 'Neither fair nor unfair'],
        [1, 'Somewhat fair'],
        [2, 'Very fair']

    ],
    )


# PAGES
class Fairness1(Page):
    form_model = 'player'
    form_fields = ['fairness']


page_sequence = [Fairness1]
