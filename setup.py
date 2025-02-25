from setuptools import setup, find_packages

setup(
    name="MyTwitter",
    version="1.0.0",
    description="Um sistema de microblogging para gerenciamento de perfis e tweets.",
    author="Seu Nome",
    author_email="seuemail@example.com",
    packages=find_packages(),
    install_requires=[
        "pytest",  # Dependência para testes automatizados
    ],
    entry_points={
        "console_scripts": [
            "mytwitter=main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)