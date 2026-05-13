class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        vals = self.keys[key]
        if timestamp < vals[0][1]:
            return ""
        if timestamp > vals[-1][-1]:
            return vals[-1][0]
        else:
            l, r = 0, len(vals) - 1
            while l <= r:
                mid = (l + r) // 2
                if vals[mid][-1] == timestamp:
                    return vals[mid][0]
                elif vals[mid][-1] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
        return vals[r][0]

# Time complexity = O(logn)
# Space complexity =  O(n)
