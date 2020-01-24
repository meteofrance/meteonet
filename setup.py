import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meteonet_toolbox",
    version="0.0.1",
    author="LabIA-MF",
    author_email="gwennaelle.larvor@meteo.fr",
    description="Data exploration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab.meteo.fr/deep_learning/data_exploration",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
