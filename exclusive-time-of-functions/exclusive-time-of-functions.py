class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        
        task = defaultdict(list)
        prevTaskId = -1
        prevTime = -1
        active = []
        for i in range (len(logs)-1):
            parts = logs[i].split(':')
            task1 = parts[0]
            status1 = parts[1]
            time1 = parts[2]
            
            parts = logs[i+1].split(':')
            task2 = parts[0]
            status2 = parts[1]
            time2 = parts[2]
            
            
            if status1=="start" and status2=="start":
                task[task1].append(int(time2) - int(time1))
                active.append(task1)
                
            elif status1=="start" and status2=="end":
                if(task1==task2):
                    task[task1].append(int(time2) - int(time1)+1)
                    
            elif status1=="end" and status2=="end":
                if(task1==task2):
                    task[task1].append(int(time2) - int(time1))
                    active.pop()
                    
                else:
                    task[task2].append(int(time2) - int(time1))
                    active.pop()
            
            elif status1=="end" and status2=="start":
                if len(active) > 0:
                    act = active.pop()
                    task[act].append(int(time2) - int(time1) - 1)
                    active.append(act)  

        res = [0]*n
        for key, val in task.items():
            res[int(key)] = sum(val)
                                    
        return (res)
            
            