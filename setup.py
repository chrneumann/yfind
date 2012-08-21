import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'docopt',
    'modgrammar',
    'pyyaml',
    ]

tests_require = [
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'pytest-xdist',
    ]

setup(name='yfind',
      version='0.1.0a2',
      description="Search YAML files satisfying specified conditions.",
      long_description='\n\n'.join([README, CHANGES]),
      classifiers=[
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Environment :: Console",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Topic :: Text Processing",
          "Topic :: Text Processing :: Markup",
      ],
      author='Christian Neumann',
      author_email='cneumann@datenkarussell.de',
      url='https://github.com/chrneumann/yfind',
      keywords='yaml find search',
      license="BSD-2-Clause",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      entry_points="""\
      [console_scripts]
      yfind = yfind:main
      """,
      extras_require={
          'testing': tests_require,
          },
      )
