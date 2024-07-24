#!/usr/bin/python3
"""Script that-unlocks list of lists"""


def canUnlockAll(boxes):
    """This function takes a list-of-lists andthe content
       of dlist will unlock-other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
