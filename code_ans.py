class Solution:
    def countIntersections(self, arr):
        """
        Counts the number of intersections of chords in a circle.

        :param arr: A tuple containing two lists, the first with radian measures 
                    and the second with corresponding 'start' and 'end' identifiers.
        :return: The total number of intersections.
        """
        start_values = {}  # Mapping from start identifiers to their radian values.
        active_starts = []  # List of tuples (identifier, radian) for active starts.
        total_intersections = 0

        for i in range(len(arr[0])):
            identifier = arr[1][i]
            radian = arr[0][i]

            if identifier.startswith('s'):
                # Store the start value and add to active starts.
                start_values[identifier] = radian
                active_starts.append((identifier, radian))
            else:
                # Find the corresponding start, count intersections, and remove from active.
                corresponding_start = 's' + identifier[1:]
                start_radian = start_values[corresponding_start]
                start_index = self.findInsertionIndex(active_starts, start_radian)
                total_intersections += len(active_starts) - start_index - 1
                active_starts.pop(start_index)

        return total_intersections

    def findInsertionIndex(self, active_starts, start_radian):
        """
        Performs a binary search to find the index at which start_radian is present in active_starts.

        :param active_starts: Sorted list of tuples (identifier, radian).
        :param start_radian: Radian value to find in active_starts.
        :return: The index of the start_radian in active_starts.
        """
        left, right = 0, len(active_starts) - 1
        while left <= right:
            mid = (left + right) // 2
            if active_starts[mid][1] == start_radian:
                return mid
            elif active_starts[mid][1] > start_radian:
                right = mid - 1
            else:
                left = mid + 1
        return left
a = Solution()
# test cases
print(a.countIntersections([(1, 2, 3, 4, 5, 6, 7, 8,9,10), ('s1', 's2', 's3', 's4', 's5', 'e3','e2', 'e1', 'e4','e5')]))

print(a.countIntersections([(1, 2, 3, 4, 5, 6), ('s1', 's2', 's3','e1','e2', 'e3')]))

print(a.countIntersections([(1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12), ('s1', 's2', 's3', 's4', 's5','s6', 'e3','e2', 'e1','e5', 'e4','e6')]))