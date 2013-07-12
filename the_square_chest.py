#checkIO

class Recorder(object):
    def __init__(self,lines=[]):
        self.Nlist = []
        for line in lines:
            if line[0] not in self.Nlist: self.Nlist.append(line[0])
            if line[1] not in self.Nlist: self.Nlist.append(line[1])
        self.Lines = [sorted(line) for line in lines]
        self.N = 4 # boundary default 4x4
        self.Num = 0

    def find_router_index(self, inipp, lenn):
        """
        find North, South, West, East boundary lists based on inipp
        inipp: ini point
        lenn : len for boundary
        ex: inipp(6)
        lenn(2)
        return : [[6,7],[7,8],[8,12],[12,16],[6,10],[10,14],[14,15],[15,16]]
        """

        if (inipp-1) / self.N  != (inipp+lenn-1) / self.N:
            return []

        return [[inipp+i, inipp+1+i] for i in xrange(lenn)] + \
        [[inipp+self.N*i, inipp+self.N*(i+1)] for i in xrange(lenn)] + \
        [[inipp+self.N*lenn+i, inipp+self.N*lenn+1+i] for i in xrange(lenn)] + \
        [[inipp+lenn+self.N*i, inipp+lenn+self.N*(i+1)] for i in xrange(lenn)]


    def iter_pat(self):
        """ iter_pat gen """
        for i in self.Nlist:
            for l in xrange(self.N):
                yield self.find_router_index(i,l)


    def run(self):
        """ run """
        for pat in self.iter_pat():
            ipass = [i for i in pat if i in self.Lines]
            if len(ipass) == len(pat) and len(pat) != 0:
                self.Num += 1
        return self.Num


def checkio(lines_list):
    """Return the qantity of squares"""

    rec = Recorder(lines_list)
    rst = rec.run()
    del rec
    return rst


if __name__ == '__main__':
    assert (checkio([[1,2],[3,4],[1,5],[2,6],[4,8],[5,6],[6,7],
                     [7,8],[6,10],[7,11],[8,12],[10,11],
                     [10,14],[12,16],[14,15],[15,16]]) == 3) , "First, from description"
    assert (checkio([[1,2],[2,3],[3,4],[1,5],[4,8],
                     [6,7],[5,9],[6,10],[7,11],[8,12],
                     [9,13],[10,11],[12,16],[13,14],[14,15],[15,16]]) == 2), "Second, from description"
    assert (checkio([[1,2], [1,5], [2,6], [5,6]]) == 1), "Third, one small square"
    assert (checkio([[1,2], [1,5], [2,6], [5,9], [6,10], [9,10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16,15], [16,12], [15,11], [11,10],
                     [10,14], [14,13], [13,9]]) == 0), "Fifth, snake"
