from setuptools import setup, find_packages

setup(
    name='dsplayer-applemusic',  
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'dsplayer',
        'aiohttp',
        'bs4',
        'yt-dlp'
    ],
    entry_points={
        'dsplayer.plugins': [
            'plugin = plugin.plugin:AppleMusicPlugin',
        ],
    },
)