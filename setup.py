from setuptools import setup

setup(
    name='Shuyaa',  
    version='0.1',  
    description='A Python module to generate random passwords',  
    url='http://github.com/MyNameIsShekhar/shuyaa',
    author='Shekhar',  
    author_email='shekharhatture20@gmail.com',  # Your email
    license='MIT',  
    packages=['Shuyaa'],
    install_requires=[
        'string',
        'random',
    ],  
    zip_safe=False 
)

