# TMS_ElectricField_Group_Simulation


# Group Analysis with SimNIBS

This repository contains a Python script to perform group analysis of TMS simulations using SimNIBS for specific subjects, both pre and post some treatment or intervention.

## Description

The script is tailored to run simulations for TMS (Transcranial Magnetic Stimulation) by setting up a coil in the C3 position. The coil used in the simulation is `Magstim_70mm_Fig8.nii.gz`, but this can be changed based on available coil definitions in SimNIBS.

Subjects are labeled with an ID followed by either `_pre` or `_post` indicating pre-intervention and post-intervention status, respectively. 

## Requirements

- Python (version as per SimNIBS compatibility)
- SimNIBS 4.0 installed and set up

## Instructions

1. **Setup**: Ensure you have SimNIBS 4.0 and the required dependencies installed.
2. **Data**: Ensure your subject data is structured correctly, especially the naming conventions. The script assumes names like 'sub-011_pre', 'sub-011_post', etc.
3. **Parameters**: The script currently uses the `Magstim_70mm_Fig8.nii.gz` coil at position `C3` with an orientation of `[0, 0, 1]`. Adjust these parameters in the script if necessary.
4. **Running the Script**: Execute the script in the environment where SimNIBS is set up. It will simulate the electric fields for all the specified subjects and save the results in the `Remy_TBS_group_analysis` directory.

## Folder Structure

The results will be saved in a directory named `Remy_TBS_group_analysis`. Inside this directory, there will be individual directories for each subject, labeled by their ID and status, e.g., `sub-011_pre`.

## Note

1. Ensure you have enough computational resources, as TMS simulations can be computationally intensive.
2. Ensure backup of any previous simulations as this script might overwrite the results if executed multiple times.
3. Adjust coil parameters (`didt`, `pos`, `moments`) as per your requirements.

## Support

For issues, questions, or modifications to this script, please raise an issue in this GitHub repository or contact the repository owner/maintainer.

## References

- [SimNIBS documentation](http://www.simnibs.org/documentation)
- [TMS coil definitions in SimNIBS](http://www.simnibs.org/doc/simnibs/_build/html/coil_files.html)



