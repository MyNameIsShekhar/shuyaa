from setuptools import setup

setup(
    name='Shuyaa',  # Name of your package
    version='0.1',  # Version number
    description='A Python module to generate random passwords',  # Short description
    url='http://github.com/MyNameIsShekhar/shuyaa',  # Link to your GitHub repository or other source
    author='Shekhar',  # Your name
    author_email='shekharhatture20@gmail.com',  # Your email
    license='MIT',  # License type
    packages=['random_password'],  # Name of directory containing __init__.py
    install_requires=[
        'string',
        'random',
    ],  # List of dependencies
    zip_safe=False  # Not necessary, but can be True or False depending on your needs
)

