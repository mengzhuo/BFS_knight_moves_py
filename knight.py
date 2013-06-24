#!/usr/bin/env python
# encoding: utf-8
"""
Author: Meng Zhuo<mengzhuo1203@gmail.com>
Version: 0.1
"""

import sys


class Point(object):

    def __init__(self, x, y, step=0, path=[]):
        """
        Point object for knight_move 

        :x: point x
        :y: point y
        :step: current step
        :returns: Point object

        """
        self.x = int(x)
        self.y = int(y)
        self.step = int(step)
        self.path = path

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__() 

    def __str__(self):
        return u"Point<{0.x}, {0.y}> step={0.step}".format(self)


def knight_move(size, pre_point, des_point):
    """
    BFS knight movement

    :param pre_point: Point that start with
    :param x: destination x
    :param y: destination y
    :returns: point that can solve problem
    """
    size = int(size)
    board = [[0 for tmp_y in xrange(size)] for tmp_x in xrange(size)]
    queue = [pre_point]  # init search queue
    rules = ((1, 2) , (2, 1), #1
             (1, -2), (2, -1), #4
             (-1, -2),(-2, -1), #3
             (-2, 1), (-1, 2)) #2
 
    while(queue):
        pre_point = queue.pop(0) # get first point
        if pre_point.x == des_point.x and pre_point.y == des_point.y:
            #for line in board:
            #    print line
            return pre_point

        for direction in rules:

            next_point = Point(pre_point.x+direction[0], 
                          pre_point.y+direction[1], 
                          pre_point.step+1,)

            if (0<= next_point.x < size and 0<= next_point.y < size
                and not board[next_point.y][next_point.x]):
                # check if new point still inside board
                # and next_point is valided
                next_point.path = pre_point.path + [next_point]
                queue.append(next_point)
                board[next_point.y][next_point.x] = 1

def usage():

    print """Knight less moves from given point to Right Bottom Corner.
Example: python knight.py -s 8 -x 1 -y 3
-h print this help message
"""
    sys.exit(1)

if __name__ == '__main__':
    import getopt
    try:
        opts = getopt.getopt(sys.argv[1:], "s:x:y:h:t:")[0]
    except getopt.GetoptError:
        usage()
    
    try:
        for opt, val in opts:
            if opt == "-s":
                size = int(val)
                assert size > 2 # only great than 3 has solution
            elif opt == "-x":
                x = int(val)
                assert size > x >= 0
            elif opt == "-y":
                y = int(val)
                assert size > y >= 0
            elif opt == "-h":
                usage()

        result = knight_move(size, Point(x, y), Point(size-1, size-1))

        if result:
            for point in result.path:
                print "step:{0.step} ({0.x},{0.y})".format(point)
        else:
            print "No solution"
    except (ValueError, AssertionError) as err:
        if err is ValueError:
            print "Please input integer"
        else:
            print "Please input positive number less than {0}".format(size)
        usage()
