from setuptools import setup, find_packages

requires = [
    "Zope2",
    "five.grok",
    "babel",
    "markupsafe",
]

setup(
    name="guestbook",
    install_requires=requires,
    packages=find_packages(),
)
