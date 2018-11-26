# -*- coding: utf-8 -*-
from aldryn_apphook_reload import __version__
from setuptools import find_packages, setup

setup(
    name='aldryn-apphook-reload',
    author='Stefan Foulis',
    author_email='stefan@foulis.ch',
    version=__version__,
    url='https://github.com/aldryn/aldryn-apphook-reload/',
    license='BSD',
    platforms=['OS Independent'],
    description='Reload urls of django CMS Apphooks without a restart',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=(
        'Django>=1.11',
    ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
