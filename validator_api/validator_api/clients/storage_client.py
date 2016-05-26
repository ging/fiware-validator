# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import os
import logging


class LocalStorage:

    def __init__(self, path="/tmp/cookbooks"):
        self.path = os.path.abspath(path)

    def list_cookbooks(self):
        """
        :return: list of all cookbooks in the current path
        """
        valid = []
        for cb in os.listdir(self.path):
            if self.check_cookbook(cb):
                valid.append(cb)
        return valid

    def list_recipes(self, cb):
        """
        :return: list of all recipes in the current cookbook
        """
        valid = []
        for rec in os.listdir(os.path.join(self.path, cb)):
            if self.check_recipe(rec):
                valid.append(rec)
        return valid

    def check_recipe(self, rec):
        return True

    def check_cookbook(self, cb):
        """
        Test if a directory contains a cookbook
        :param cb: directory name
        :return: test result
        """
        logging.info("checking %s" % cb)
        check = False
        # check if the item is a directory
        cb_path = os.path.join(self.path, cb)
        if os.path.isdir(cb_path):
            # check if the item has a recipes directory
            if os.path.isdir(os.path.join(cb_path, "recipes")):
                check = True
                logging.debug("Cookbook found: %s" % cb)
        if not check:
            logging.debug("Not a cookbook: %s" % cb)
        return check

if __name__ == '__main__':
    import sys
    logging.basicConfig(level=logging.DEBUG)
    c = LocalStorage(path=sys.argv[1])
    print c.list_cookbooks()
