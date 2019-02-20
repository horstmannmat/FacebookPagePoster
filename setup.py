import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FacebookPagePoster",
    version="0.1.3",
    author="Matheus Horstmann",
    author_email="mch15@c3sl.ufpr.br",
    description="A bot to post of facebook pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/horstmannmat/FacebookPagePoster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
