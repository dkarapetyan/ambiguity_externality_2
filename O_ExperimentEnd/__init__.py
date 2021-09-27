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
        player.participant.random_part = random.randint(1,3)


# PAGES
class Hidden(Page):
    timeout_seconds = 0

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        print(player.session.config['name'])
        if player.session.config['name'] == "perp":
            player.participant.payoff_final = [player.participant.payoff_ext, player.participant.payoff_noext, player.participant.payoff_choice][player.participant.random_part-1]
            player.participant.performance_final = int([player.participant.performance_ext, player.participant.performance_noext, player.participant.performance3][player.participant.random_part-1])
            player.participant.payoff_pounds = cu(player.participant.payoff_final * 0.05)
        if "victim" in player.session.config['name']:
            player.participant.payoff_total = cu((max(player.participant.payoff_final,
                                                      0) + player.participant.dictator) * 0.05)


class YThanks(Page):
    def is_displayed(player: Player):
        return "victim" in player.session.config['name']


class Redirect(Page):
    pass


class BThanks(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"


page_sequence = [Hidden, BThanks, YThanks, Redirect]
