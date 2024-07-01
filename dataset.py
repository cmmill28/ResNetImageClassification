import numpy as np
import pandas as pd
import torch
from PIL import Image as Im
from torch.utils.data import Dataset

np.random.seed(42)

class CustomDataset(Dataset):
    def __init__(self, subset, transform):
        self.subset = subset
        self.transform = transform

    def __getitem__(self, idx):
        x, y = self.subset[idx]
        if self.transform:
            x = self.transform(x)
        return self.subset.indices[idx], x, y  # first element is the list of indices from the original dataset

    def __len__(self):
        return len(self.subset)

class CombinedDataset(Dataset):
    """
    pos_samples: csv file containing positive sample files
    neg_samples: csv file containing negative sample files
    n_samples: number of samples to contain in the dataset
    label_ratio: positive/negative sample ratio
    """

    def __init__(self,
                 pos_samples,
                 neg_samples,
                 n_samples=None,
                 label_ratio=0.5,
                 transform=None):
        self.pos_samples = pd.read_csv(pos_samples, nrows=n_samples)
        self.neg_samples = pd.read_csv(neg_samples, nrows=n_samples)
        self.label_ratio = label_ratio
        self.transform = transform

    def __getitem__(self, idx):
        label = 1 if np.random.rand() < self.label_ratio else 0
        if label:
            img_file = self.pos_samples.iloc[idx]['filepath']
        else:
            img_file = self.neg_samples.iloc[idx]['filepath']
        image = Im.open(img_file).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, label

    def __len__(self):
        return min(len(self.pos_samples), len(self.neg_samples))
