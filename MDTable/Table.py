

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

    def add_data(self, data: list):
        """Add data to table"""
        if isinstance(data, list):
            self.data = data

    def add_row(self, row: list):
        """Add row to table"""
        if isinstance(row, list):
            self.data.append(row)

    def add_column(self,name:str, column: list):
        """Add column to table"""
        if isinstance(column, list):
            if len(column) == len(self.data):
                for i in range(len(column)):
                    self.data[i].append(column[i])
                self.header.append(name)
            else:
                raise ValueError("Column length must match data length")
            
    def __str__(self) -> str:
        """Return table as string"""
        table = "|"
        for i in self.header:
            table += " " + str(i) + " |"
        table += "\n"
        for i in range(len(self.header)):
            table += "| --- "
        table += "|\n"
        for i in self.data:
            table += "|"
            for j in i:
                table += " " + str(j) + " |"
            table += "\n"
        return table

        
        

    
