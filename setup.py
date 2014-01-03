#-*- coding: utf-8 -*-

import codecs

version = __import__('osmapi').__version__

description = codecs.open('README.md', encoding='utf-8').read()
try:
    import pypandoc
    from unidecode import unidecode
    description = unidecode(description)
    description = pypandoc.convert(description, 'rst', format='md')
except (IOError, ImportError):
    pass

from distutils.core import setup
setup(
    name='osmapi',
    packages=['osmapi'],
    version=version,
    description='Python wrapper for the OSM API',
    long_description=description,
    author=u'Etienne Chové',
    author_email='chove@crans.org',
    maintainer='Stefan Oderbolz',
    maintainer_email='odi@readmore.ch',
    url='https://github.com/metaodi/osmapi',
    download_url='https://github.com/metaodi/osmapi/archive/v%s.zip' % version,
    keywords=['openstreetmap', 'osm', 'api'],
    license='GPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries',
        'Development Status :: 4 - Beta',
    ],
)
