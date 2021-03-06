# basic tools for doing ml

class TwoDArray(object): # yes, I know everything exists in numpy already.
    """A basic 2d array
    
    >>> arr = TwoDArray(2, 2) 
    >>> print arr # doctest: +NORMALIZE_WHITESPACE
    [
    	[0, 0],
    	[0, 0]
    ]
    >>> arr2 = TwoDArray(2, 2, [[1, 1], [2, 3]])
    >>> print arr2 # doctest: +NORMALIZE_WHITESPACE
    [
    	[1, 1],
    	[2, 3]
    ]
    >>> print arr + arr2 # doctest: +NORMALIZE_WHITESPACE
    [
    	[1, 1],
    	[2, 3]
    ]
    >>> print arr - arr2 # doctest: +NORMALIZE_WHITESPACE
    [
    	[-1, -1],
    	[-2, -3]
    ]
    >>> print arr[0, 0]
    0
    >>> print arr2[1, 1]
    3
    >>> arr2[1, 1] = -30; print arr2[1, 1]
    -30
    >>> arr3 = TwoDArray(2, 3, [[1, 1], [2, 5], [3, 4]])
    >>> print arr3 # doctest: +NORMALIZE_WHITESPACE
    [
    	[1, 1],
    	[2, 5],
    	[3, 4]
    ]
    >>> arr = [TwoDArray(1, 2, [[1], [2]]), TwoDArray(2, 1, [[54, 21]])]
    >>> print arr[0] # doctest: +NORMALIZE_WHITESPACE
    [
    	[1],
    	[2]
    ]
    >>> print arr[1] # doctest: +NORMALIZE_WHITESPACE
    [
    	[54, 21]
    ]
    >>> print arr[0] * arr[1] # doctest: +NORMALIZE_WHITESPACE
    [
        [96]
    ]  
    >>> print arr[1] * arr[0] # doctest: +NORMALIZE_WHITESPACE
    [
    	[54, 54],
    	[42, 42]
    ]
    """
    def __init__(self, m, n, array=None):
        self.m = m
        self.n = n
        
        if array:
            self._array = [[array[j][i] for i in xrange(m)] for j in xrange(n)]
        else:
            self._array = [[0 for i in xrange(m)] for j in xrange(n)]
    
    def singular_value_decomposition(self):
        u, sig, v_star = 0, 0, 0
        pass
    
    pinv = singular_vaue_decomposition
        
    def __str__(self):
        return "[\n\t{}\n]".format(',\n\t'.join(str(data_set) for data_set in self._array))
        
    def normalize_1d_data(self, data, range_func=None):
        if range_func:
            r = float(range_func(data))
        else:
            r = float(max(data) - min(data))
        mean = sum(data) / float(len(data))
        
        return [(item - mean) / r for item in data]
    
    def copy(self):
        return TwoDArray(self.m, self.n, self._array)
    
    def __foreach(self, func, copy, other):
        for n in xrange(self.n):
            for m in xrange(self.m):
                copy[n, m] = func(copy[n, m], other[n, m])
     
    def normalize(self):
        ret = self.copy()
        
        for n, data_set in enumerate(self._array):
            ret._array[n] = self.normalize_1d_data(data_set)
        
        return ret
        
    def __getitem__(self, tup):
        return self._array[tup[0]][tup[1]]
    
    def __setitem__(self, tup, value):
        self._array[tup[0]][tup[1]] = value
   
    @staticmethod
    def __add(obj1, obj2):
        return obj1 + obj2
        
    @staticmethod
    def __sub(obj1, obj2):
        return obj1 - obj2
        
    def __identical_check(self, other):
        if other.m != self.m and other.n != self.n:
            raise Exception("Arrays are not of same dimensions!")
    
    def __add__(self, other):
        self.__identical_check(other)

        ret = self.copy()

        self.__foreach(self.__add, ret, other)
               
        return ret
        
    def __sub__(self, other):
        self.__identical_check(other)

        ret = self.copy()

        self.__foreach(self.__sub, ret, other)
               
        return ret            
        
    def __mul__(self, other):
        if other.n != self.m:
            raise Exception("Arrays are not of same dimensions for multiplication!")

        ret = TwoDArray(self.m, other.n)

        for n in xrange(other.n):
            for m in xrange(self.m):
                for k in xrange(self.n):
                    ret[n, m] += self[k, n] * other[n, k]

        return ret
        
    def __rmul__(self, other):
        if self.n != other.m:
            raise Exception("Arrays are not of same dimensions for multiplication!")

        ret = TwoDArray(other.m, self.n)

        for n in xrange(self.n):
            for m in xrange(other.m):
                for k in xrange(self.n):
                    print n, m, self[n, k] * other[k, n]
                    ret[n, m] += self[n, k] * other[k, n]

        return ret
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
