import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Java_Final_Project-Josie-Ravisha-Nidhi",
    version="0.0.1",
    author="Josie Schmitt, Ravisha Jaiswal, and Nidhi Kamath",
    author_email="90302872@ep-student.org",
    description="Our chat bot for final project",
    long_description=long_description,
    long_description_content_type="markdown",
    url="https://github.com/amybird200/Java_Final_Project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)