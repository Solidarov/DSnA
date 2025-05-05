class Hashmap:

    def __init__(self, size):
        self.size = size
        self.table = self.__create_table(size)


    def __create_table(self, size):
        return [[] for _ in range(size)]
    

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.table[hashed_key]

        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[idx] = (key, value)
        else:
            bucket.append((key, value))
    

    def find_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.table[hashed_key]

        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
        if found_key:
            return record_value
        else:
            return "No record found"
        

    def del_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.table[hashed_key]

        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(idx)
        
        return found_key
        

    def show_table(self):
        table = "{\n"
        for bucket in self.table:
            if not bucket:
                continue
            else:
                for items in bucket:
                    table += f"\t{items[0]}: {items[1]},\n"

        table += "}"
        return table


