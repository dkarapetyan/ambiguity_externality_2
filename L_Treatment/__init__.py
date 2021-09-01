import random

from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'L_Treatment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    information = models.BooleanField()


def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.information = random.choice([True, False])
        print('information is ', player.information)

# PAGES


class InfoTreatment(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.information and player.session.config['name'] == "victim1"


page_sequence = [InfoTreatment]
