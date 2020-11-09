#!/usr/bin/env python

import numpy as np

mask = np.random.rand(len(df)) < 0.8
train = df[mask]
test = df[~mask]
