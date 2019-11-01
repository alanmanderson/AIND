from utils import *

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    for square,options in values.iteritems():
        if len(options) == 1:
            for peerSquare,peers in peers:
                for peer in range(len(peers)):
		    values[peer].replace('options', '')
