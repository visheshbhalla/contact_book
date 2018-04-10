from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'pymongo',
    'pyramid_debugtoolbar',
    'pytest',
    'mock'
]

setup(name='contact_book',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = contact_book:main
      """,
)

