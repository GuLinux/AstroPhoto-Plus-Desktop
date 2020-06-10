#!/usr/bin/env python3
import os
import sys
import shutil
import requests
import subprocess
import hashlib

os_name = os.environ.get('TRAVIS_OS_NAME', 'linux')
qt5_version = os.environ.get('QT5_VERSION', '5.15.0')
qt5_shortversion = qt5_version.replace('.', '')

if len(sys.argv) != 2:
    raise RuntimeError('Usage: {} <destination-path>'.format(sys.argv[0]))

destination = sys.argv[1]
if os.path.exists(destination):
    shutil.rmtree(destination)

files = {
    'windows': {
        'os': 'windows_x86',
        'compiler': 'win64_msvc2017_64',
        'build': '-0-202002260536',
        'packages': [
            { 'qtpackage': '', 'filename':             'qtbase-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtmultimedia-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtdeclarative-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtwebchannel-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtlocation-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtserialport-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qttools-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
            { 'qtpackage': '.qtwebengine', 'filename': 'qtwebengine-Windows-Windows_10-MSVC2017-Windows-Windows_10-X86_64.7z'},
        ],
    },
    'linux': {
        'os': 'linux_x64',
        'compiler': 'gcc_64',
        'build': '-0-202005140804',
        'packages': [
            { 'qtpackage': '', 'filename':             'qtmultimedia-Linux-RHEL_7_6-GCC-Linux-RHEL_7_6-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtdeclarative-Linux-RHEL_7_6-GCC-Linux-RHEL_7_6-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtbase-Linux-RHEL_7_6-GCC-Linux-RHEL_7_6-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtwebchannel-Linux-RHEL_7_6-GCC-Linux-RHEL_7_6-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtlocation-Linux-RHEL_7_6-GCC-Linux-RHEL_7_6-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtserialport-Linux-RHEL_7_6-GCC-Linux-RHEL_7_6-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'icu-linux-Rhel7.2-x64.7z'},
            { 'qtpackage': '.qtwebengine', 'filename': 'qtwebengine-Linux-RHEL_7_6-GCC-Linux-RHEL_7_6-X86_64.7z'},
        ],
    },
    'osx': {
        'os': 'mac_x64',
        'compiler': 'clang_64',
        'build': '-0-202005140805',
        'packages': [
            { 'qtpackage': '', 'filename':             'qtbase-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtdeclarative-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtmultimedia-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtwebchannel-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtlocation-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qtserialport-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
            { 'qtpackage': '', 'filename':             'qttools-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
            { 'qtpackage': '.qtwebengine', 'filename': 'qtwebengine-MacOS-MacOS_10_13-Clang-MacOS-MacOS_10_13-X86_64.7z'},
        ],
    },
}

print('os name: {}'.format(os_name))
print('qt5 version: {} ({})'.format(qt5_version, qt5_shortversion))

url_pattern = 'https://download.qt.io/online/qtsdkrepository/{os}/desktop/qt5_{qtshort}/qt.qt5.{qtshort}{qtpackage}.{compiler}/{qtver}{qtbuild}{filename}'

os.makedirs(destination, exist_ok=True)

os_files = files[os_name]
for package in os_files['packages']:
    settings = { 'os': os_files['os'], 'qtshort': qt5_shortversion, 'qtver': qt5_version, 'qtbuild': os_files['build'], 'compiler': os_files['compiler'] }
    settings.update(package)
    filename = settings['filename']
    url = url_pattern.format(**settings)

    sha1_response = requests.get('{}.sha1'.format(url))
    sha1_response.raise_for_status()
    sha1_response = sha1_response.text.strip()
    print('Downloading {}, SHA1: {}'.format(filename, sha1_response))

    response = requests.get(url)
    response.raise_for_status()
    with open(os.path.join(destination, filename), 'wb') as destfile:
        destfile.write(response.content)

    sha1 = hashlib.sha1()
    with open(os.path.join(destination, filename), 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha1.update(data)
    if not sha1.hexdigest() == sha1_response:
        raise RuntimeError('Wrong SHA1 For {}: expected: {}, downloaded: {}'.format(filename, sha1_response, sha1.hexdigest()))
    print('SHA1 check passed for {}'.format(filename))

    extract_result = subprocess.run(['7z', 'x', filename], cwd=destination)
    extract_result.check_returncode()

    os.remove(os.path.join(destination, filename))
