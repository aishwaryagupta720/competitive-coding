class Solution:
    # queue [interval,items] heap [items]
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks=list(Counter(tasks).values())
        tasks=[-i for i in tasks]
        heapq.heapify(tasks)
        queue=deque()
        interval=0
        while tasks or queue:
            interval+=1
            if queue and queue[0][0]<interval:
                heapq.heappush(tasks,-1*queue.popleft()[1])
            if tasks:
                task=-1*(heapq.heappop(tasks))
                task-=1
                if task>0:
                    queue.append([interval+n,task])
        
        return interval
        
            




# We use heap because we need to exhaust the task with greater occurance first to reduce time taken (descending order of occurance)
# we use queue to keep track of idle time between tasks, once the desired time has passed we put it back in heap and select by occurance
#  we cannot use the same heap because heap only gives us the top most (biggest) value , and if the interval is not right for that value we cannot go to the next value , I tried sorting my interval but was not getting optimum time taken