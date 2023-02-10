import inquirer

from .aws import get_sso_sessions, run_sso_login, write_temp_credentials

def cli():
    questions = [
        inquirer.List(
            'profile',
            message="Select AWS profile",
            choices=get_sso_sessions(),
        ),
        inquirer.Confirm(
            'write_temp_creds',
            message="Write temp credentials to ~/.aws/credentials?",
            default=True,
        ),
    ]

    answers = inquirer.prompt(questions)
    profile = answers['profile']
    temp_creds_profile = None

    if answers['write_temp_creds']:
        questions = [
            inquirer.Text(
                'profile',
                message="Profile name",
                default="default",
            ),
        ]

        answers = inquirer.prompt(questions)
        temp_creds_profile = answers['profile']

    run_sso_login(profile)
    write_temp_credentials(temp_creds_profile)
