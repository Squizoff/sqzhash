from setuptools import setup, find_packages

# Read the contents of README.md for long description
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sqzhash',
    version='1.0.3',
    description='SqzHash is a custom cryptographic hash algorithm implementation designed to compute hash values for strings and files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_repository',
    author='Squizoff',
    packages=find_packages(),
    python_requires='>=3.6',
)