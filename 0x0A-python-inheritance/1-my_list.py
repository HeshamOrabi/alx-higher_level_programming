#!/usr/bin/python3
"""

    class MyList that inherits from list

"""


class MyList(list):
    """MyList that inherits from list"""
    def print_sorted(self):
        """print list in ascending order"""
        tmp = self.copy()
        for i in range(len(tmp)):
            for j in range(i + 1, len(tmp)):
                if int(tmp[i]) > int(tmp[j]):
                    tmp[i], tmp[j] = tmp[j], tmp[i]
        print(tmp)
