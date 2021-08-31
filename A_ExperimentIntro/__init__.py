from otree.api import *

c = Currency

doc = """
Experimental introductory pages
"""


class Constants(BaseConstants):
    name_in_url = 'UEAIntro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific = models.StringField(label="Your Prolific ID:", max_length=24)
    consent = models.IntegerField(
        choices=[
            [1, "I consent"],
            [2, "I do not consent"]
        ]
    )

# PAGES


class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific']

    @staticmethod
    def error_message(player, values):
        error_msg = dict()
        if len(values['prolific']) != 24:
            error_msg = 'Your Prolific ID should be 24 characters long'
        return error_msg


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']


class BlockDropouts(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.consent == 2


class BlueIntro(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"


class BlueIntro2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "perp"


class Yellow1Intro(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] != "perp"


class Yellow2Intro(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] != "perp"


page_sequence = [Welcome, Consent, BlockDropouts, BlueIntro, BlueIntro2, Yellow1Intro, Yellow2Intro]
