# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

import json


class LinkUtil:
    @staticmethod
    def load_links(file_path):
        with open(file_path) as f:
            loaded_links = json.load(f)
        return loaded_links


