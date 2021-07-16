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

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.part_rate = 2
        player.participant.externality_II = 0
        player.participant.ext_choice = 1
        if player.session.config['name'] == "victim":
            player.participant.ext_choice = int(Constants.rows[random.randint(0, (len(Constants.rows) - 1))]['R_PartII_EncryptionTask.1.player.externality'])
            print('externality choice is', player.participant.ext_choice)
            player.participant.externality_II = (2-player.participant.ext_choice)*(int(Constants.rows[random.randint(
                0, (len(Constants.rows) - 1))]['R_PartII_EncryptionTask.1.player.performance']))
        else:
            if player.participant.externality_II == 2:
                player.part_rate = 1.6
        player.participant.payoff_II = max((player.participant.performance_II-player.participant.externality_II)*player.part_rate, 0)


class ChoiceTreatment(Page):
    pass


page_sequence = [Hidden, ChoiceTreatment]
