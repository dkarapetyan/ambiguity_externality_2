from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'N_Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    fairness = models.IntegerField(
        choices=[
            [-2, 'Very unfair'],
            [-1, 'Somewhat unfair'],
            [0, 'Neither fair nor unfair'],
            [1, 'Somewhat fair'],
            [2, 'Very fair']
        ],
    )

    enjoyment = models.IntegerField(
        choices=[
            [-2, 'Very unenjoyable'],
            [-1, 'Somewhat unenjoyable'],
            [0, 'Neither enjoyable nor unenjoyable'],
            [1, 'Somewhat enjoyable'],
            [2, 'Very enjoyable']
        ],
    )


# PAGES
class YellowSurvey(Page):
    @staticmethod
    def is_displayed(player: Player):
        return "victim" in player.session.config['name']

class BlueSurvey(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"

page_sequence = [YellowSurvey, BlueSurvey]