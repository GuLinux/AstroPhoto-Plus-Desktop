#!/usr/bin/env python3
from github import Github
from github.GithubException import UnknownObjectException
import os
import sys
import traceback
import time

with open('release.env', 'w') as release_env:
    release_env.write('export RELEASES_NAME="{}"\n'.format('**** TEST pr.title'))
    release_env.write('export RELEASES_RELEASE_NOTES_FILE="release_notes.md"\n')
with open('release_notes.md', 'w') as release_notes:
    release_notes.write('**** test release notes')


