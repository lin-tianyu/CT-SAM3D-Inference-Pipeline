"""
*** 1. converting BDMAP (Demo with vertebrae) label to DAP label, and also chaneg storing format
    2. postprocessing using DAP method
    3. use to generate point for CT-SAM3D
"""

import numpy as np
import nibabel as nib
import os, sys
import glob
import csv
from tqdm import tqdm


if __name__ == "__main__":
    BDMAP_path = "/root/autodl-tmp/AbdomenAtlasDemoPredictSource"
    SAVE_path = "/root/autodl-tmp/AbdomenAtlasDemoPredictSourceDAPformat"
    DAP_csv_path = "../Data/label_name.csv"

    with open(DAP_csv_path, "r") as f:
        DAP_label_name = dict(csv.reader(f))


    volume_paths = glob.glob(os.path.join(BDMAP_path, "*", "combined_labels.nii.gz"))
    for volume_path in tqdm(volume_paths):
        volume_name = volume_path.split("/")[-2]
        label_nii = nib.load(volume_path)
        affine, header = label_nii.affine, label_nii.header
        label_data = label_nii.get_fdata().astype(np.uint8)

        for i, j in enumerate(range(66, 42, -1)):
            i += 1
            label_data[label_data==i] = j

        processed_nii = nib.Nifti1Image(label_data.astype(np.uint8), affine, header)
        nib.save(processed_nii, 
                 os.path.join(SAVE_path, f"{volume_name}.nii.gz"))
        # break

