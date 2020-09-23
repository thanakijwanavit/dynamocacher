import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynamocacher",
    version="0.0.7",
    author="Nic Wanavit",
    author_email="nwanavit@gmail.com",
    description="storing cache using dynamodb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thanakijwanavit/dynamocacher",
    packages=['dynamocacher'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ['pynamodb-dax']
)
