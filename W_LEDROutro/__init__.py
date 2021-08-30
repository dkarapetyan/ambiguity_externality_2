import random

from otree.api import *

author = 'LEDR Team'

doc = """
outro
"""


class Constants(BaseConstants):
    name_in_url = 'outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def creating_session(subsession):
    for player in subsession.get_players():
        player.participant.random_part = random.choice(['I', 'II'])


#PAGES

class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.session.config['name'] == "perp":
            if player.participant.random_part == 'I':
                player.participant.payoff = player.participant.payoff_I
            else:
                player.participant.payoff = player.participant.payoff_II
        else:
            pass


class Y1Thanks(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim1"

class Y2Thanks(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim2"


class BThanks(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"


page_sequence = [Hidden, BThanks, Y1Thanks, Y2Thanks]
