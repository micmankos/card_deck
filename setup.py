import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sg_deck-micmankos", # Replace with your own username
    version="1.0.0",
    author="Michael Mankos",
    author_email="micmankos@gmail.com",
    description="A small implementation of a card deck",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/micmankos/sg_card_deck",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)