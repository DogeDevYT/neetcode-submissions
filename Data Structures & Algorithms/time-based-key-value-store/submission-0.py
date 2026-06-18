"""
Ok I think for this problem, the KEY haha key is to realize we can store a LIST of values with timestamps somehow
at an associated hashmap value example "alice": [("sonion", 3), ("gurt", 2)]

ok I think I got it, since we have strictly increasing timestamps, we can get away with just append to the list of 
tuples associated with each key and then do binary search on that in get()
"""
class TimeMap:

    def __init__(self):
        self.swag = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if we already have smth, just append to list
        if key in self.swag:
            self.swag[key].append((value, timestamp))
        else: #otherwise create new list with value element + timestamp tuple
            self.swag[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        #create return variable
        res = ""

        if key in self.swag:
            #basic binary search
            arr = self.swag[key]

            l,r = 0, len(arr) - 1

            while (l <= r):
                mid = (l+r)//2

                if arr[mid][1] <= timestamp:
                    #add correct timestamp factor instead of incorrect factor
                    res = arr[mid][0]

                    #keep executing in case we find smth better
                    l = mid + 1 #try to find smth closer
                else:
                    r = mid - 1 #converge towards timestamp
        return res

