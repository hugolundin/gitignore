# gitignore

A python script for creating .gitignore files more easily. It is a convenience wrapper around the api for 
gitignore.io.

## Installation

Start by installing the requirements:

```bash
$ pip3 install -r requirements.txt
```

### Using the script as a git extension

Add the following to your `.gitconfig` (replacing `path_to_repository` with the location
where this project has been put):

```bash
ignore = "!gipy() { python3 <path_to_repository>/gitignore.py $@;}; gipy"
```

## Usage

Give wanted templates as a comma-separated list argument:

```bash
$ git ignore swift,python,macos,linux > .gitignore
```

Alternatively, if you do not use the git extension:

```bash
$ python3 gitignore.py swift,python,macos,linux > .gitignore
```
