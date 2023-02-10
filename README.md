# aws-sso-wrangler

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/jsynowiec/aws-sso-wrangler/blob/master/LICENSE)

A tiny tool for controlling many AWS SSO profiles. It'll help you to quickly sign using `aws sso` and write temporary credentials under a selected profile in `~/.aws/credentials`.

## Installation

First, instal the AWS CLI v2 and configure your SSO profiles. Then install this tool using `pipx`:

    pipx install git+https://github.com/jsynowiec/aws-sso-wrangler

## Usage

```sh
$ aws-sso-wrangler
[?] Select AWS profile: CompanyA-ProfileA
 > CompanyA-ProfileA
   CompanyA-TeamB-ProfileA
   CompanyA-TeamB-ProfileB

[?] Write temp credentials to ~/.aws/credentials? (Y/n): Y

[?] Profile name: default
Attempting to automatically open the SSO authorization page in your default browser.

Temporary credentials written to ~/.aws/credentials under [default] profile.
Credentials will expire at 2023-02-01T21:10:01Z
```
