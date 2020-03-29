# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from ..util.coordinate import Coordinate


class Bee(Coordinate):

    def __init__(self, **kwargs) -> None:  # pylint:disable=useless-super-delegation
        """
        Initializes a new instance of the Bee class
        """
        super().__init__(**kwargs)
