class Matrix(object):
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = None

    def __repr__(self):
        return "[" + "\n".join([str(row) for row in self.data]) + "]"

    def __str__(self):
        return "[" + "\n".join([str(row) for row in self.data]) + "]"

    @staticmethod
    def array(data):
        assert type(data) == list and data is not None
        matrix = Matrix()
        if type(data[0]) == list:
            matrix.cols = len(data[0])
            matrix.rows = len(data)
        else:
            matrix.cols = len(data)
            matrix.rows = 1
        matrix.data = data
        return matrix

    def shape(self):
        return (self.rows, self.cols)

    def _fill_val(self, val):
        self.data = [[val for j in range(self.cols)] for i in range(self.rows)]

    @staticmethod
    def ones(rows, cols):
        assert rows != 0 and cols !=0
        matrix = Matrix()
        matrix.rows = rows
        matrix.cols = cols
        matrix._fill_value(1.0)
        return matrix

    @staticmethod
    def zeros(rows, cols):
        assert rows != 0 and cols != 0
        matrix = Matrix()
        matrix.rows = rows
        matrix.cols = cols
        matrix._fill_value(0.0)
        return matrix
    
    def __add__(self, m):
        assert isinstance(m, Matrix)
        assert self.rows == m.rows and self.cols == m.cols
        matrix = Matrix()
        matrix.rows = m.rows
        matrix.cols = m.cols
        """
        matrix._fill_val(0.0)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                data[i][j] = self.data[i][j] + m.data[i][j]
        """
        matrix.data = [[self.data[i][j] + m.data[i][j] for j in range(matrix.cols)] for i in range(matrix.rows)]
        return matrix


    def __sub__(self, m):
        assert isinstance(m, Matrix)
        assert self.rows == m.rows and self.cols == m.cols
        matrix = Matrix()
        matrix.rows = m.rows
        matrix.cols = m.cols
        """
        matrix._fill_val(0.0)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                data[i][j] = self.data[i][j] - m.data[i][j]
        """
        matrix.data = [[self.data[i][j] - m.data[i][j] for j in range(matrix.cols)] for i in range(matrix.rows)]
        return matrix

    @staticmethod
    def dot(m1, m2):
        assert isinstance(m1, Matrix) and isinstance(m2, Matrix)
        assert m1.cols == m2.rows
        matrix = Matrix()
        matrix.rows = m1.rows
        matrix.cols = m2.cols
       
        matrix._fill_val(0.0)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                for k in range(m2.rows):
                    matrix.data[i][j] += m1.data[i][k] * m2.data[k][j]
        
        return matrix

    def __mul__(self, m):
        assert isinstance(m, Matrix)
        assert self.rows == m.rows and self.cols == m.cols
        matrix = Matrix()
        matrix.rows = self.rows
        matrix.cols = self.cols
        """
        matrix._fill_val(0.0)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                matrix.data[i][j] = self.data[i][j] * m.data[i][j]
        """
        matrix.data = [[self.data[i][j] * m.data[i][j] for j in range(matrix.cols)] for i in range(matrix.rows)]
        return matrix
