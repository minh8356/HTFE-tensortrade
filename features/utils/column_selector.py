# Copyright 2019 The TensorTrade Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License
import os
import sys
ttpath = os.path.abspath('..')
sys.path.append(ttpath)

import numpy as np
import pandas as pd

from typing import Union, List

from tensortrade.features.transformer import Transformer, TransformableList


class ColumnSelector(Transformer):
    """A transformer for selecting named columns within a feature pipeline."""

    def __init__(self, columns: Union[List[str], str]):
        """
        Arguments:
            columns: A list of column keys to be selected from the pipeline.
        """
        self._columns = columns

    def transform(self, X: TransformableList, y: TransformableList = None):
        return X[self._columns]
