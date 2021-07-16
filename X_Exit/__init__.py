import random

from otree.api import *

author = ''

doc = """
Redirect to Prolific"""


class Constants(BaseConstants):
    name_in_url = 'redirect'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


#PAGES

class Redirect(Page):
    pass


page_sequence = [Redirect]
