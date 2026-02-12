import os
from setuptools import setup, find_packages

# Get the current directory path
HERE = os.path.abspath(os.path.dirname(__file__))

def load_requirements(file_name):
    """
    Safely load requirements from a text file.
    Filters out comments, empty lines, and pip flags.
    """
    requirements = []
    path = os.path.join(HERE, file_name)
    
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # Skip empty lines, comments, and recursive requirements/editable flags
                if not line or line.startswith("#") or line.startswith("-"):
                    continue
                requirements.append(line)
    return requirements

setup(
    name="DeepMRIAge",
    url="https://github.com/BAICIL/AgePredication",
    version="0.1.0",
    author="Javad Sohankar, Banner Alzheimer's Institute, j.sohankar@{bannerhealth.com, gmail.com}",
    description="Predicting Chronological Age based on 3D Brain MRI Images using Deep Learning models (utilizing ResNet18 architecture)",
    packages=find_packages(),
    # Dynamically inject the filtered list here
    install_requires=load_requirements("requirements.txt"),
    python_requires=">=3.11",
)
