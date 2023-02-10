import configparser
import glob
import json
import subprocess
from os import environ

HOME = environ["HOME"]


def get_sso_sessions():
    config = configparser.ConfigParser()
    config.read(f"{HOME}/.aws/config")

    return [
        p.removeprefix("profile ") for p in config.sections() if p.startswith("profile")
    ]


def run_sso_login(profile: str):
    try:
        proc = subprocess.run(
            f"aws sso login --profile {profile}",
            shell=True,
            check=True,
            capture_output=True,
            encoding="utf8",
        )
        proc.check_returncode()
        print(proc.stdout)
    except subprocess.CalledProcessError as err:
        # TODO: Handle errors
        pass


def write_temp_credentials(profile: str):
    cli_creds = []
    for fname in glob.glob(f"{HOME}/.aws/cli/cache/*.json"):
        with open(fname, "r") as f:
            cli_creds.append(json.load(f)["Credentials"])

    cli_creds = sorted(cli_creds, key=lambda d: d["Expiration"], reverse=True)
    newest_creds = cli_creds[0]

    config_file = f"{HOME}/.aws/credentials"
    config = configparser.ConfigParser()
    config.read(config_file)

    config[profile] = {
        "aws_access_key_id": newest_creds["AccessKeyId"],
        "aws_secret_access_key": newest_creds["SecretAccessKey"],
        "aws_session_token": newest_creds["SessionToken"],
    }

    with open(config_file, "w") as f:
        config.write(f)

    print(
        f"Temporary credentials written to ~/.aws/credentials under [{profile}] profile.\n"
        f"Credentials will expire at {newest_creds['Expiration']}"
    )
