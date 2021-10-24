from otree.api import *
import csv
import random
import os

doc = """
a.k.a. Encryption Game
"""


class Constants(BaseConstants):
    data_path_csv = os.path.join("G_EncryptTask_1", "bluematch.csv")
    with open(data_path_csv, encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    players_per_group = None
    name_in_url = "encrypt1"
    num_rounds = 2
    letters_per_word = 5
    use_timeout = True
    seconds_per_period = 360


class Subsession(BaseSubsession):
    dictionary = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    performance = models.FloatField(initial=0)
    mistakes = models.IntegerField(initial=0)
    bonus = models.IntegerField(initial=0)
    earnings = models.CurrencyField(initial=0)
    bonus_question = models.CurrencyField(initial=0)
    final = models.CurrencyField(initial=0)
    tokens = models.FloatField()
    blue_ext = models.IntegerField()
    externality = models.IntegerField(initial=0)
    initial_ans = models.StringField(initial="")
    num_wrong = models.IntegerField(initial=0)
    inst_path = models.StringField()
    externality_imposed = models.IntegerField()

    # Perpetrator with externality
    p_ext_q1 = models.IntegerField(
        label="Your earnings will be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    p_ext_q2 = models.IntegerField(
        label="You are randomly and anonymously paired with a new Yellow player for each Encryption task.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    p_ext_q3 = models.IntegerField(
        label="How many tokens will you earn for each word you encrypt correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    p_ext_q4 = models.IntegerField(
        label="How many tokens will the Yellow player lose for every word you encrypt correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )

    # Perpetrator with no externality
    p_noext_q1 = models.IntegerField(
        label="Your earnings will be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    p_noext_q2 = models.IntegerField(
        label="How many tokens will you earn for each word you encrypt correctly?",
        choices=[[1, "1.5"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    p_noext_q3 = models.IntegerField(
        label="How many tokens will the Yellow player lose for every word you encrypt correctly?",
        choices=[[1, "1"], [2, "0"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    p_noext_q4 = models.IntegerField(
        label="How many tokens will you lose for for every word the Yellow player encrypts "
              "correctly?",
        choices=[[1, "1"], [2, "0"], [3, "4"]],
        widget=widgets.RadioSelect
    )

    # Victim 1
    v1_q1 = models.IntegerField(
        label="Your earnings will be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v1_q2 = models.IntegerField(
        label="You are randomly and anonymously paired with a Blue player.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v1_q3 = models.IntegerField(
        label="How many tokens will you earn for each word you encrypt correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    v1_q4 = models.IntegerField(
        label="How many tokens will you lose for each word the Blue player encrypted correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )

    # Victim 2 Control
    v2_c_q1 = models.IntegerField(
        label="Your earnings are expected to be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v2_c_q2 = models.IntegerField(
        label="You are randomly and anonymously paired with a Blue player.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v2_c_q3 = models.IntegerField(
        label="The computer program will have randomly assigned one of two payoff schemes to your matched Blue "
              "player.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v2_c_q4 = models.IntegerField(
        label="How many tokens will you earn for each word you encrypt correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    v2_c_q5 = models.IntegerField(
        label="How many tokens will you lose for each word the Blue player encrypts correctly if the computer program "
              "assigned "
              "the payoff scheme that could have decreased your earnings?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )

    # Victim 2 Treatment
    v2_t_q1 = models.IntegerField(
        label="Your earnings will be higher the better your performance is.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v2_t_q2 = models.IntegerField(
        label="You are randomly and anonymously paired with a Blue player.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v2_t_q3 = models.IntegerField(
        label="Your matched Blue player will have made a choice between two payoff schemes.",
        choices=[[1, "True"], [2, "False"]],
        widget=widgets.RadioSelect
    )
    v2_t_q4 = models.IntegerField(
        label="How many tokens will you earn for each word you encrypt correctly?",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )
    v2_t_q5 = models.IntegerField(
        label="How many tokens will you lose for each word you encrypt correctly if your matched Blue player chose "
              "the payoff scheme that decreases your earnings? ",
        choices=[[1, "1"], [2, "2"], [3, "4"]],
        widget=widgets.RadioSelect
    )


# PAGES
class EarningsInstructions_v1(Page):
    form_model = "player"
    form_fields = ["v1_q1", "v1_q2", "v1_q3", "v1_q4"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(v1_q1=1, v1_q2=1, v1_q3=2, v1_q4=1, )
        error_messages = dict()

        for field_name in solutions:
            if len(player.initial_ans) < 6:
                player.initial_ans += str(values[field_name])
            if values[field_name] != solutions[field_name]:
                player.num_wrong += 1
                error_messages[field_name] = 'Wrong answer.'

        return error_messages

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.name == "victim1"


class EarningsInstructions_v2_c(Page):
    form_model = "player"
    form_fields = ["v2_c_q1", "v2_c_q2", "v2_c_q3", "v2_c_q4", "v2_c_q5"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(v2_c_q1=1, v2_c_q2=1, v2_c_q3=1, v2_c_q4=2, v2_c_q5=1,)
        error_messages = dict()

        for field_name in solutions:
            if len(player.initial_ans) < 6:
                player.initial_ans += str(values[field_name])
            if values[field_name] != solutions[field_name]:
                player.num_wrong += 1
                error_messages[field_name] = 'Wrong answer.'

        return error_messages

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.name == "victim2" and not player.participant.v2_treatment


class EarningsInstructions_v2_t(Page):
    form_model = "player"
    form_fields = ["v2_t_q1", "v2_t_q2", "v2_t_q3", "v2_t_q4", "v2_t_q5"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(v2_t_q1=1, v2_t_q2=1, v2_t_q3=1, v2_t_q4=2, v2_t_q5=1, )
        error_messages = dict()

        for field_name in solutions:
            if len(player.initial_ans) < 6:
                player.initial_ans += str(values[field_name])
            if values[field_name] != solutions[field_name]:
                player.num_wrong += 1
                error_messages[field_name] = 'Wrong answer.'

        return error_messages

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.name == "victim2" and player.participant.v2_treatment


class BeginEncryptionTask(Page):
    pass


class Task(Page):
    form_model = "player"
    form_fields = ["performance", "mistakes"]
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {
            "legend_list": legend_list,
            "task_list": task_list,
            "task_width": task_width,
        }


class Complete(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.tokens = 2 * player.performance
        matchrow = random.randint(0, (len(Constants.rows) - 1))
        player.participant.bluematch = Constants.rows[matchrow]['participant.code']
        if player.participant.name == "victim1":
            if Constants.rows[matchrow]['G_EncryptTask_1.1.player.blue_ext'] == 0:
                player.externality = int(Constants.rows[matchrow]['G_EncryptTask_1.1.player.performance'])
            else:
                player.externality = int(Constants.rows[matchrow]['G_EncryptTask_1.2.player.performance'])
        else:
            if player.participant.v2_treatment:
                player.externality = int(Constants.rows[matchrow]['J_EncryptTask_2.1.player.performance'])*(1-int(Constants.rows[matchrow]['J_EncryptTask_2.1.player.ext_choice']))
                player.participant.externality_imposed = 1 - int(Constants.rows[matchrow]['J_EncryptTask_2.1.player.ext_choice'])
            else:
                player.externality = int(Constants.rows[matchrow]['G_EncryptTask_1.1.player.performance'])*(
                        1-int(Constants.rows[matchrow]['G_EncryptTask_1.1.player.blue_ext']))
                player.externality_imposed = 1-int(Constants.rows[matchrow]['G_EncryptTask_1.1.player.blue_ext'])
                player.participant.externality_imposed = 1-int(Constants.rows[matchrow]['G_EncryptTask_1.1.player.blue_ext'])
        player.participant.externality = player.externality
        player.participant.payoff_final = player.tokens - player.externality


class Earnings(Page):
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if "victim" in player.participant.name:
            return "H_BeliefElicitation"


class GenInstructions_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number==1

page_sequence = [
    EarningsInstructions_v1,
    EarningsInstructions_v2_c,
    EarningsInstructions_v2_t,
    BeginEncryptionTask,
    Task,
    Complete,
    Earnings,
    GenInstructions_2
]
