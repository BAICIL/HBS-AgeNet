# Age Predication based on 3D MRI Images
###Javad Sohankar (j.sohankar@bannerhealth.com)
###Banner Alzheimer's Institute, Phoenix, Arizona, US

We trained three deep learning models (based on ResNet18 architecture) to predict chronological age from structural T1-weighted MRI scans. The three models (HeadAge, BrainAge, SkullAge) were trained based on three different types of MRI image: 1) Head (including skull and facial features), 2) Brain only, 3) Skull only. 

Training process used data from five data sets (ABIDE, ICBM, IXI, NACC, OASIS; N=7932), and then evaluated on a separate dataset (ADNI, N=11007).

First, raw T1-MRI scans were processed using FreeSurfer 7 software. For HeadAge model, “nu.mgz" files were used as head image for training and afterward evaluating it. Similarly, BrainAge model used “brain.mgz” files for training/evaluation.  For SkullAge model, we started with extracting the skull portion based on "nu.mgz" (head image) and "brain.mgz" (brain image), and saved them to disk. Afterwards these skull images were used for training and testing the SkullAge model.

## Installing The Package  
We have implemented and tested the model on python 3.11. For installing dependencies, you can choose between these three methods:

1) Use the "requirements.txt" file, and install depenendices using
```
pip install -r requirements.txt
```

2) run the "setup.py" script which fetches the libraries from the "requirements.txt" file and installs them.
```
python3 setup.py
```

3) 

## Running The Package  
