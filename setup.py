from kiki_algoritms import (
    __version__ as version,
    __name__ as name,
    __license__ as license,
    __author__ as author
)

import setuptools

setuptools.setup(
    name = name,
    version = version,
    description = '제가 아는 알고리즘들을 활용한 함수들을 모아놓는 모듈이에요!',
    long_description = open('README.md', 'r', encoding = 'utf-8').read(),
    long_description_content_type = 'text/markdown',
    license = license,
    author = author,
    url = 'https://github.com/kiki7000/kiki_algorithms',
    author_email = 'devkiki7000@gmail.com',
    packages = setuptools.find_packages(),
    keywords = ['kiki', 'sort', 'fibonacci', 'algoritms'],
    python_requires = '>=3.6',
    install_requires = ['asyncio'],
    zip_save = False
)