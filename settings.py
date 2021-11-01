from os import environ


SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.05,
    'participation_fee': 2.50,
    'doc': "",
}
PARTICIPANT_FIELDS = ['nettokens',
                      'externality',
                      'externality1',
                      'externality2',
                      'externality3',
                      'ext_choice',
                      'payoff_final',
                      'payoff_ext',
                      'payoff_noext',
                      'payoff_choice',
                      'externality_imposed',
                      'performance_ext',
                      'performance_noext',
                      'performance3',
                      'performance_final',
                      'dictator',
                      'random_part',
                      'failedattentioncheck',
                      'bluematch',
                      'v2_treatment',
                      'blue_ext',
                      'payoff_total',
                      'payoff_pounds',
                      'name'
                      ]

SESSION_CONFIGS = [
   dict(
        name="Yellow",
        display_name="Yellow",
        num_demo_participants=1,
        completionlink="https://app.prolific.co/submissions/complete?cc=20B7F325",
        app_sequence=['A_ExperimentIntro',
                      'B_Attention_1',
                      'C_GenInstructions_1',
                      'D_EncryptPractice',
                      'E_Attention_2',
                      'F_PlayerRoles',
                      'G_EncryptTask_1',
                      'H_BeliefElicitation',
                      'K_Attention_3',
                      'L_Treatment',
                      'M_Dictator',
                      'N_Survey',
                      'O_ExperimentEnd'
                      ],
    ),
]

ROOMS = [
    dict(
        name='Session_Y',
        display_name='Yellow Players II',
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '09f!o3#&@=4o$@-_vas++o8hv6#9te_c&+cq$w6mp#jl&1qbd('

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
