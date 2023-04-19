

class Table:
    """Markdown Table Generator"""


    def __init__(self, **kwargs):
        """Initialize Table object"""
        self.header = []
        self.data = []

        if 'header' in kwargs:
            if isinstance(kwargs['header'], list):
                self.header = kwargs['header']
            else:
                raise TypeError("Header must be a list")

        if 'data' in kwargs:
            if isinstance(kwargs['data'], list):
                if len(kwargs['data']) > 0:
                    if isinstance(kwargs['data'][0], list):
                        self.data = kwargs['data']
                    else:
                        raise TypeError("Data must be a list of lists")
                else:
                    raise ValueError("Data must contain at least one row")
            else :
                raise TypeError("Data must be a list of lists")

    
    def add_header(self, header: list):
        """Add header to table"""
        if isinstance(header, list):
            self.header = header
        else:
            raise TypeError("Header must be a list")

    def add_data(self, data: list):
        """Add data to table"""
        if isinstance(data, list):
            if len(data) > 0:
                if isinstance(data[0], list):
                    self.data = data
                else:
                    raise TypeError("Data must be a list of lists")
            else:
                raise ValueError("Data must contain at least one row")
        else:
            raise TypeError("Data must be a list of lists")

    def add_row(self, row: list,*args):
        """Add row to table"""
        if isinstance(row, list):
            if len(row) == len(self.header):
                self.data.append(row)
            else:
                raise ValueError("Row length must match header length")
        else:
            raise TypeError("Row must be a list")
        if args:
            for i in args:
                if isinstance(i, list):
                    if len(i) == len(self.header):
                        self.data.append(i)
                    else:
                        raise ValueError("Row length must match header length")
                else:
                    raise TypeError("Row must be a list")

    def add_column(self,name:str, column: list):
        """Add column to table"""
        if isinstance(column, list):
            if len(column) == len(self.data):
                for i in range(len(column)):
                    self.data[i].append(column[i])
                self.header.append(name)
            else:
                raise ValueError("Column length must match data length")
        else:
            raise TypeError("Column must be a list")
            
    def __str__(self) -> str:
        """Return table as string"""
        tableSize = [self.__get_size_of_column(i) for i in range(len(self.header))]
        table = "|"
        for i in range(len(self.header)):
            table += " " + self.header[i] + " "*(tableSize[i] - len(self.header[i])) + " |"
        table += "\n|"
        for i in range(len(self.header)):
            table += "-"*(tableSize[i] + 2) + "|"
        table += "\n"
        for i in self.data:
            table += "|"
            for j in range(len(i)):
                table += " " + str(i[j]) + " "*(tableSize[j] - len(str(i[j]))) + " |"
            table += "\n"
        return table



    def __get_size_of_column(self, column: int) -> int:
        """Return size of column"""
        size = 0
        for i in self.data:
            if len(str(i[column])) > size:
                size = len(str(i[column]))
        if len(self.header[column]) > size:
            size = len(self.header[column])
        return size
        
        

    
