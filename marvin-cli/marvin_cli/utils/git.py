import os

def git_init(path):
    os.chdir(path)
    os.system(' '.join(['git', 'init', '.']))

def bump_version(part, verbose, dryrun):
    command = ['bump2version', part]
    if verbose:
        command.append('--verbose')
    if dryrun:
        command.append('--dry-run')
    os.system(' '.join(command))

