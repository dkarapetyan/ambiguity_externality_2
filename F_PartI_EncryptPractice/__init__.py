from otree.api import *

doc = """
a.k.a. Encryption Game
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = "encrypt_practice"
    fixed_amount = 0.8
    letters_per_word = 5
    use_timeout = True
    seconds_per_entr = 120
    seconds_per_period = 120


class Subsession(BaseSubsession):
    dictionary = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    performance_entr = models.IntegerField(initial=0)
    mistakes_entr = models.IntegerField(initial=0)
    performance = models.IntegerField(initial=0)
    mistakes = models.IntegerField(initial=0)
    valeur = models.IntegerField(initial=0)
    bonus = models.IntegerField(initial=0)
    earnings = models.CurrencyField(initial=0)
    bonus_question = models.CurrencyField(initial=0)
    final = models.CurrencyField(initial=0)
    disp_ext = models.BooleanField()


# PAGES

class Example(Page):
    pass


class RolesTokens(Page):
    pass


class TaskEntrainement(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = "player"
    form_fields = ["performance_entr", "mistakes_entr"]
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_entr

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {
            "legend_list": legend_list,
            "task_list": task_list,
            "task_width": task_width,
        }


class ResultsEntr(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    Example,
    RolesTokens,
    TaskEntrainement,
    ResultsEntr,
]
