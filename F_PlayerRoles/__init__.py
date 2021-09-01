from otree.api import *

doc = """Player Roles"""


class Constants(BaseConstants):
    name_in_url = 'Player_Roles'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class PlayerRoles(Page):
    pass


page_sequence = [
    PlayerRoles,
    ]
