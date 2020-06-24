class ACCOUNTS():
    def __init__(self):
        self.CodeChef = {
            "username": "username",
            "password": "password"
        }

        self.Hackerrank = {
            "username": "username",
            "password": "password",
            "tracks":  ["python"]
            # Available (add as per your requirements):
            #   Languages: "java", "python", "c", "cpp", "ruby", "shell", "sql", "fp",
            #   Domians: "algorithms", "data-structures", "mathematics", "ai", "databases", "regex"
            #            "tutorials"
        }

    def getAccounts(self):
        return vars(self)
