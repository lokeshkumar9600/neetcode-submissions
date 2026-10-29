class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
         x, y, z = target

         first = second = third = False

         for a, b, c in triplets:
            # Ignore triplets that exceed the target
            if a > x or b > y or c > z:
                continue

            # Track which target values we can obtain
            if a == x:
                first = True
            if b == y:
                second = True
            if c == z:
                third = True

         return first and second and third

        