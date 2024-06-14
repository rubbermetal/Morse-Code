cat <<EOL > setdup.py
from setuptools import setup, find_packages

setup(
    name='txt-morse',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'pygame',
    ],
    include_package_data=True,
)
EOL
