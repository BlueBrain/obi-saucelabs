# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

import json
import requests


class LinkChecker:
    def __init__(self):
        self.valid_status_codes = range(200, 500)

    def check_link_status(self, link):
        response = requests.head(link)
        status_code = response.status_code
        return status_code in self.valid_status_codes

    @staticmethod
    def load_links(file_path):
        with open(file_path, 'r') as file:
            links = json.load(file)
        return links

    def check_links(self, links_to_check):
        for link in links_to_check:
            is_valid = self.check_link_status(link)
            if is_valid:
                print(f"Link is valid: {link}")
            else:
                print(f"Broken link found: {link}")