# better time complexity
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        buckets=0
        hamsters = list(hamsters)
        for i in range(len(hamsters)):
            fed=False
            if hamsters[i]=='H': # if a hamster
                if i-1>=0 : # if left exists
                    if hamsters[i-1]=='.' : # if left is empty
                        if i+1>=len(hamsters) or hamsters[i+1]=='H': # only if right does not exist or right is full FILL LEFT
                            buckets+=1
                            hamsters[i-1]='B'
                            fed=True
                    elif hamsters[i-1]=='B': # if left is  bucket then hamster if fed
                        fed=True
                # right check should not depend on if left exists or not
                if i+1<len(hamsters) and not fed: # if right exists and hamster is not fed
                    if hamsters[i+1]=='.': # if right is empty then add bucket
                        buckets+=1
                        hamsters[i+1]='B'
                        fed=True
                
                if not fed: # if still not fed
                    return -1
                
                
                    
        return buckets


                    
# constant space complexity
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        buckets=0
        last_bucket_pos=-1
        for i in range(len(hamsters)):
            fed=False
            if hamsters[i]=='H':
                if i-1>=0 :
                    if hamsters[i-1]=='.' and last_bucket_pos!=i-1:
                        if i+1>=len(hamsters) or hamsters[i+1]=='H':
                            buckets+=1
                            last_bucket_pos=i-1
                            fed=True
                    elif i-1==last_bucket_pos:
                        fed=True

                if i+1<len(hamsters) and not fed:
                    if hamsters[i+1]=='.' and last_bucket_pos!=i+1:
                        buckets+=1
                        last_bucket_pos=i+1
                        fed=True
                
                if not fed:
                    return -1
                
                
                    
        return buckets


                    
                    

        
        

# 2086. Minimum Number of Food Buckets to Feed the Hamsters
