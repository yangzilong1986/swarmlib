# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

# pylint: disable=unused-variable,unused-argument
# to do remove

class Firefly():
    def __init__(self, alpha, beta, gamma, position):
        self.__position = position


    @property
    def position(self):
        return self.__position
