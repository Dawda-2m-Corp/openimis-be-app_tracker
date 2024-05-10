from setuptools import setup

setup(
    name='openimis-be-app_tracker',
    version='0.1.0',
    install_requires=[
        'Django>=3.2.4',
        'django-easy-audit==1.3.6',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Topic :: Office/Business :: Financial :: Accounting',
    ],
    author='Dawda Borje Kujabi',
    author_email='dkujabi@2m-corp.com',
    description='Django application to track and manage apps versions',
    # url='https://github.com/openimis/openimis-be-app_tracker',
    keywords='openimis django app version tracker',
)
