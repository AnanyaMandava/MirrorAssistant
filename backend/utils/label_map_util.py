# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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
# limitations under the License.
# ==============================================================================

"""Label map utility functions."""

import logging

import tensorflow as tf
from google.protobuf import text_format
import protos.string_int_label_map_pb2 as string_int_label_map_pb2


def _validate_label_map(label_map):
    """Checks if a label map is valid.

    Args:
      label_map: StringIntLabelMap to validate.

    Raises:
      ValueError: if label map is invalid.
    """
    for item in label_map.item:
        if item.id < 1:
            raise ValueError('Label map ids should be >= 1.')


def create_category_index(categories):
    """Creates dictionary of COCO compatible categories keyed by category id.

    Args:
      categories: a list of dicts, each of which has the following keys:
        'id': (required) an integer id uniquely identifying this category.
        'name': (required) string representing category name
          e.g., 'cat', 'dog', 'pizza'.

    Returns:
      category_index: a dict containing the same entries as categories, but keyed
        by the 'id' field of each category.
    """
    category_index = {}
    for cat in categories:
        category_index[cat['id']] = cat
    return category_index



def send_video():
    if VISION is not None:
        VISION.image_queue.put(request.data.decode("utf-8").split(';base64,')[1][:-1])
        return jsonify(success=True)
    else:
        return jsonify(success=False)

