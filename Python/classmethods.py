class laptop:
    storage_type="ssd"

    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type: {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.ram} RAM {self.storage} {self.storage_type}")

l1=laptop("16gb","512gb")
l2=laptop("8gb","256gb")

l1.get_info()
l2.get_info()