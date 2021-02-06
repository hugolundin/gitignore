import colorama
import requests
import sys
import re

def error(message):
    print(f'{colorama.Fore.RED}Error:{colorama.Style.RESET_ALL} {message}')
    exit(1)

def warning(message):
    print(f'{colorama.Fore.YELLOW}Warning:{colorama.Style.RESET_ALL} {message}')
    exit(1)

def invalid_message(words):
    if not words:
        return ""    

    if len(words) == 1:
        return f"'{words[0]}' is not a valid template."
    else:
        description = "{} and '{}'".format(', '.join("'{0}'".format(w) for w in words[:-1]), words[-1])
        return f'{description} are not valid templates.'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        error('Invalid number of arguments given.')

    response = requests.get(f'https://www.toptal.com/developers/gitignore/api/{sys.argv[1]}')

    if response.status_code == 404:
        invalid = []

        for line in response.text.splitlines():
            match = re.search(r'ERROR: (\S+)', line)

            if match:
                invalid.append(match.group(1))

        count = len(invalid)

        if len(invalid) > 0:
            warning(invalid_message(invalid))
        else:
            error('Invalid response from server.')

    print(response.text)

