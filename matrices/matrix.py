class Matrix:
    """ Class to create and manipulate Matrices 
    
    Allows the operation of summation, subtraction and multiplication between 
    Matrix objects
    """

    def __init__(self, rows:int, columns:int, values:list):
        """ Initializes the data

        :param rows: number of matrix rows
        :type rows: int
        :param columns: number of matrix columns
        :type rows: int
        :param values: values that make up the matrix
        :type rows: list
        """
        self.rows = rows
        self.columns = columns
        self.values = values
    
    @property
    def values(self) -> list:
        """ Getter for Matrix values 

        :return: values that make up the matrix
        :rtype: list
        """
        return self._values

    @values.setter
    def values(self, new_values:list):
        """ Setter for Matrix values
        
        Arranges values in matrix format according to number of columns

        :param new_values: values that make up the matrix
        :type new_values: list
        """
        matrix = []
        row = []
        for value in new_values:
            row.append(value)
            if len(row) == self.columns:
                matrix.append(row.copy())
                row.clear()
        self._values = matrix.copy()

    def __repr__(self) -> str:
        """ Arranges rows in matrix format

        :return: rows in matrix format
        :rtype: str
        """
        matrix = ''
        for row in self.values:
            matrix += f'{row}\n'
        return matrix
    
    def __add__(self, other:'Matrix') -> 'Matrix':
        """ Performs the sum between Matrix objects

        :param other: the other matrix that will be part of the operation
        :type other: Matrix

        :return: the sum of the matrices
        :rtype: Matrix
        """
        return self.add_and_sub(other)
    
    def __sub__(self, other:'Matrix') -> 'Matrix':
        """ Performs subtraction between Matrix objects

        :param other: the other matrix that will be part of the operation
        :type other: Matrix

        :return: the subtraction of the matrices
        :rtype: Matrix
        """
        return self.add_and_sub(other, False)

    def __mul__(self, other:'Matrix') -> 'Matrix':
        """ Performs multiplication between Matrix objects

        :param other: the other matrix that will be part of the operation
        :type other: Matrix

        :return: the multiplication of the matrices
        :rtype: Matrix
        """
        result_values = []
        for row in self.values:
            for column in range(other.columns):
                new_value = 0
                for value_index, value in enumerate(row):
                    new_value += value * other.values[value_index][column]
                result_values.append(new_value)
        return Matrix(self.rows, other.columns, result_values)
                
    def add_and_sub(self, other:'Matrix', sum:bool=True) -> 'Matrix':
        """ Performs the sum or subtraction between Matrix objects

        :param other: the other matrix that will be part of the operation
        :type other: Matrix
        :param sum: defines whether the arrays will be summed or subtracted
        :type param: bool
        
        :return: resulting from the operation
        :rtype: Matrix
        """
        result_values = []
        for row_index, row in enumerate(self.values):
            for value_index, value in enumerate(row):
                if sum:
                    new_value = value + other.values[row_index][value_index]
                else:
                    new_value = value - other.values[row_index][value_index]
                result_values.append(new_value)
        return Matrix(self.rows, self.columns, result_values)
