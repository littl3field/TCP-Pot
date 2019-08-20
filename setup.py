from setuptools import setup

def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data

setup(
    name='TCP-Pot',
    version='1.0.0',
    description='A TCP Honeypot',
    long_description=readme_file_contents(),
    author='littl3field',
    author_email='littl3field@protonmail.com',
    license='MIT',
    packages=['tcp-pot'],
    #scripts=['bin/tcp-pot', 'bin/tcp-pot.bat']
    zip_safe=False,
    install_requires=[
        'docopt'
    ]
)