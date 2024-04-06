class Solution:
    def reorganizeString(self, s: str) -> str:
        # The heap keeps the characters in order of occurance , to get optimum solution , while we use the queue to temporarily remove the character after using it so we dont reuse it , in every iteration , the previous queue element is put back in heap
        chars=Counter(list(s))
        heap=[]
        for k,v in chars.items():
            heap.append([-1*v,k])
        heapq.heapify(heap)

        queue=deque()
        ans=""
        while heap:
            char=heapq.heappop(heap)
            ans+=char[1]
            char[0]+=1
            if queue:
                heapq.heappush(heap,queue.popleft())
            if char[0]<0:
                queue.append(char)
        if not heap and queue:
            return ""
        else:
            return ans
            



# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""

        