from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my_math_utils",
    version="0.0.1",
    author="Your Name",
    author_email="your_email@example.com",
    description="A small package for basic math operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/my_math_utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
