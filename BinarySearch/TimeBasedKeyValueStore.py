class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        sspace=self.hashmap[key]
        if not sspace:
            return ""
        # assuming search space is in increasing order
        string="".join(["z"]*101)
        index=bisect.bisect_right(sspace,(timestamp,string))
        if index>0 and sspace[index-1][0]<=timestamp:
            return sspace[index-1][1]
        else:
            print("else")
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)