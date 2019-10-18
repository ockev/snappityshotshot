from setuptools import setup

setup(
    name='snappityshotshot',
    version='0.1',
    author="Kevin O'Connor",
    author_email="koconn89@gmail.com",
    description="SnappityShotShot is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/ockev/snappityshotshot",
    install_requires=[
    'click',
    'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
