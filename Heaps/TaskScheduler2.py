class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        dir = defaultdict(int)
        for task in tasks:
            dir[task]=0
        interval=0
        tasks=deque(tasks)
        while tasks:
            interval+=1
            if dir[tasks[0]]<interval:
                dir[tasks[0]]=interval+space
                tasks.popleft()
            else:
                # jumping to the required interval because of sequential execution , so cannot execute any other task
                interval=dir[tasks[0]]
        return interval



        

        