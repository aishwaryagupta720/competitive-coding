class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit =[]
        alpha=[]
        for log in logs:
            if log[-1].isalpha():
                alpha.append(log)
            else:
                digit.append(log)
        sortable=defaultdict(list)
        for i in range(len(alpha)):
            id,log = alpha[i].split(" ",1)
            sortable[log].append(id)
        ans = []
        keys = sorted(list(sortable.keys()))
        for key in keys:
            if len(sortable[key])>1:
                sortable[key]=sorted(sortable[key])
            for val in sortable[key]:
                ans.append(val+' '+key)
        return ans+digit





# 937. Reorder Data in Log Files
# Solved
# Medium
# Topics
# Companies
# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.