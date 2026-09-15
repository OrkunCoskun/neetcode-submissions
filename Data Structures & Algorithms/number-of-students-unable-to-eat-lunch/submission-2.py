class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)
        
        for sw in sandwiches:
            if cnt[sw] > 0:
                res -= 1
                cnt[sw] -= 1
            else:
                return res
        return res