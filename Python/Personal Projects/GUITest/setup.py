from setuptools import setup

APP=['legendRemade.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    option={'py2app': OPTIONS},
    setup_requires=['py2app']
)