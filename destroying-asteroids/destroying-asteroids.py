class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids = sorted(asteroids)


        while asteroids:
            a = bisect.bisect(asteroids, mass)
            if a==0:
                return False
            else:
                mass = mass + asteroids[a-1]
                asteroids.pop(a-1)
                
                
        return True