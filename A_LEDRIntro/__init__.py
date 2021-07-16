from otree.api import *

c = Currency

author = 'LEDR Team'

doc = """
Standard welcome pages for LEDR experiments
"""


class Constants(BaseConstants):
    name_in_url = 'A_LEDRIntro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific = models.StringField(label="Your Prolific ID:", max_length=24)


# PAGES

class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific']

    @staticmethod
    def error_message(player, values):
        error_msg=dict()
        if len(values['prolific']) != 24:
            error_msg = 'Your Prolific ID should be 24 characters long'
        return error_msg


page_sequence = [Welcome]
