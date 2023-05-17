class DynamicRecord():
    def __init__(self, data, queries):
        self.data = data
        self.queries = queries
        
    # this is lazy query
    def query(self, left, operation, right):
        # support AND, not support OR
        self.queries.append([left, operation, right])
        return self
    
    def run(self):
        return_data = []
        for row in self.data:
            is_match = True
            for query in self.queries:
                left = query[0]
                operation = query[1]
                right = query[2]
                if operation == '=':
                    if not row[left] == right:
                        is_match = False
                        break
            if is_match == True:
                return_data.append(row)
        return return_data

if __name__ == "__main__":
    books_data = [
        {
            "id": 1,
            "name": "Duy Book",
            "city": "Ha Noi"
        },
        {
            "id": 2,
            "name": "Le Book",
            "city": "HCM"
        },
        {
            "id": 3,
            "name": "Duy Le Book",
            "city": "HCM"
        }
    ]
    queries = [["id", "=", 2], ["city", "=", "HCM"]]
    books = DynamicRecord(
        books_data,
        queries
    )
    print(books.run())