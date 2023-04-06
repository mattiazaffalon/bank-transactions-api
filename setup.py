from setuptools import setup, find_packages

setup(
    name='bank_transactions_api',
    version='0.1.0',
    description='A package for handling bank transactions through an API',
    author='Mattia Zaffalon',
    author_email='mattia.zaffalon@gmail.com',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn[standard]',
        'pydantic',
        'sqlalchemy',
        'mysql-connector-python',
        'cloud-sql-python-connector==1.2.1',
        'pymysql'
    ],
    entry_points={
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
