#!/usr/bin/python3
"""

    class int iverted

"""


class MyInt(int):
    """class int iverted"""
    def __eq__(self, other):
        """rev"""
        return super().__ne__(other)

    def __ne__(self, other):
        """rev"""
        return super().__eq__(other)
