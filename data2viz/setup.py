from setuptools import setup, find_packages

setup(
    name='data2viz',
    version='0.1.0',
    description='A library for data visualization and interactive widgets',
    author='ta9ko',
    author_email='ibvb699@gmail.com',
    url='https://github.com/ta9ko/data2viz',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.0',
        'plotly>=5.0.0',
        'ipywidgets>=7.0.0',
        'SQLAlchemy>=1.3.0'
    ],
    extras_require={
        'dev': [
            'pytest',
            'sphinx',
            'wheel'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
