class HashMap:
    # Constructor
    # Spacetime complexity is O(1)
    def __init__(self, capacity=10):
        self.map = []
        for _ in range(capacity):
            self.map.append([])

    # Create a new hash key BigO -> O(1)
    def create_hash_key(self, key):
        return int(key) % len(self.map)

    # Insert value into hash table -> O(n)
    def insert(self, key, value):
        key_hash = self.create_hash_key(key)
        key_value = [key, value]

        if self.map[key_hash] == None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Updates hash table -> O(n)
    def update(self, key, value):
        key_hash = self.create_hash_key(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('An error has occurred while updating on key: ' + key)

    # Gets value with matching key from hash table -> O(n)
    def get_value(self, key):
        key_hash = self.create_hash_key(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # removes a value from hash table
    # runtime -> O(n)
    def delete(self, key):
        key_hash = self.create_hash_key(key)

        if self.map[key_hash] == None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item
