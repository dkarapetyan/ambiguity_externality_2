from otree.api import *
import csv
import random
import os

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'T_PartII_Treatments'
    players_per_group = None
    num_rounds = 1
    data_path = os.path.join("I_PartI_RevealEarnings", "bluematch.csv")
    with open(data_path, encoding='utf-8') as file:
        rows = list(csv.DictReader(file))

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice_info = models.BooleanField()
    part_rate = models.CurrencyField()


def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.choice_info = random.choice([True, False])
        print('choice information is ', player.choice_info)


# PAGES
class Hidden(Page):
    timeout_seconds = 0
    pass


class ChoiceTreatment(Page):
    def is_displayed(player: Player):
        return player.session.config['name'] == "victim2"


page_sequence = [Hidden, ChoiceTreatment]
