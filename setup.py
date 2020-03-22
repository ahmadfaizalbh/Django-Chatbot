from setuptools import setup, find_packages

version = __import__('django_chatbot').__version__

setup(
    name='django-chatbot',
    version=version,
    author='Ahmad Faizal B H',
    author_email='ahmadfaizalbh726@gmal.com',
    url='https://github.com/ahmadfaizalbh/django-chatbot',
    description='Django webhook for ChatBotAI',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='django chatbot ai webhook and django wrapper for ChatBotAI',
    packages=['django.chatbot', 'django.chatbot.migrations'],
    package_dir={'django.chatbot': 'django_chatbot', 'django.chatbot.migrations': 'django_chatbot/migrations'},
    include_package_data=True,
    package_data={},
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
              'chatbotAI'
    ]
)
