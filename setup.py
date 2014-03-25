from setuptools import setup, find_packages
import os

version = '3.2.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'uploadify', 'test_uploadify.txt')
    + '\n' +
    read('CHANGES.rst'))

setup(
    name='js.uploadify',
    version=version,
    description="Fanstatic packaging of uploadify.js.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Thomas Massmann',
    author_email='thomas.massmann@it-spir.it',
    url='https://github.com/tmassman/js.uploadify',
    download_url='http://pypi.python.org/pypi/js.uploadify',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'uploadify = js.uploadify:library',
        ],
    },
)
