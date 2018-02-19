# basic tools for doing ml

class TwoDArray(object): # yes, I know everything exists in numpy already.
    def __init__(self, m, n, array=None):
        self.m = m
        self.n = n
        
        if array:
            self._array = [[array[j][i] for i in xrange(m)] for j in xrange(n)]
        else:
            self._array = [[0 for i in xrange(m)] for j in xrange(n)]
    
    def singular_value_decomposition(twoDarray):
        u, sig, v_star = 0, 0, 0
        pass
        
    def normalize_1d_data(self, data, range_func=None):
        if range_func:
            r = float(range_func(data))
        else:
            r = max(data) - min(data)
        mean = sum(data) / float(len(data))
        
        return [(item - mean) / r for item in data]
    
    def copy(self):
        return TwoDArray(self.m, self.n, self._array)
    
    def __foreach(self, func, copy, other):
        for n in xrange(self.n):
            for m in xrange(self.m):
                copy._array[n][m].func(other[n][m])
     
    def normalize(self):
        ret = self.copy()
        
        #f
        
        return ret
        
    def __getitem__(self, tup):
        return self._array[tup[0]][tup[1]]
    
    def __setitem__(self, tup, value):
        self._array[tup[0]][tup[1]] = value
        
    def __add__(self, other):
        if other.m != self.m and other.n != self.n:
            raise Exception("Arrays are not of same dimension")
        
        ret = self.copy()
        
        self.__foreach(self, __add__, ret, other)
               
        return ret
                
        
    def __mul__(self, other):
        pass
        
    def __rmul__(self, other):
        pass
