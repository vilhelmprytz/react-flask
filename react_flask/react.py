####################################################################
#                                                                  #
# react-flask                                                      #
# Copyright (C) 2020, Vilhelm Prytz, <vilhelm@prytznet.se>, et al. #
#                                                                  #
# Licensed under the terms of the MIT license, see LICENSE.        #
# https://github.com/VilhelmPrytz/react-flask                      #
#                                                                  #
####################################################################

from os import walk
from os.path import join as path_join
from os.path import isdir


class React:
    def __init__(self, templates_folder="templates", precache=True, render_all=True):
        """
        Initiates react-flask

        Args:
            templates_folder (str): Name of folder where templates are stored.
            precache (bool): Build React components and save them in memory before serving (prod).
            render_all (bool): Render all .js files in templates folder.

        Raises:
            :py:class:`FileNotFoundError`
                If templates folder does not exist
        """

        self._files = []

        if not isdir(templates_folder):
            raise FileNotFoundError("specified templates folder does not exist")

        if render_all:
            for root, dirs, files in walk(templates_folder):
                for file in files:
                    if file.endswith(".js"):
                        self._files.append(path_join(root, file))
