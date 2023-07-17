import os
from setuptools import setup, find_packages

requirements = []
with open("./requirements.txt", "r") as r_file:
    requirements = r_file.read().splitlines()

def get_version():
    with open("./phyloformer/__init__.py", "r") as file:
        for line in file:
            if line.startswith("__version__"):
                 return line.split('"')[1]
    return "unknown"

setup(
    name="phyloformer",
    version=get_version(),
    description="Fast and accurate Phylogeny estimation with self-attention Networks",
    long_description=open("./README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lucanest/Phyloformer",
    author="Luca Nesterenko, Bastien Boussau, Laurent Jacob",
    license="CeCIL",
    packages=find_packages(),
    install_requires=requirements,
    package_data={
        "phyloformer": [
            os.path.join("pretrained_models", "*"),
            "LICENSE",
        ],
    },
    include_package_data=True,
    python_requires=">=3.7, <3.10",
    entry_points={
        "console_scripts": [
            "train_phyloformer = phyloformer.scripts.train:main",
            "simulate_trees = phyloformer.scripts.simulateTrees:main",
            "simulate_alignments = phyloformer.scripts.simulateAlignments:main",
            "make_tensors = phyloformer.scripts.make_tensors:main",
            "predict = phyloformer.scripts.predict:main",
            "evaluate = phyloformer.scripts.evaluate:main",
        ]
    },
)
