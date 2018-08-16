"""
Merge overlapping intervals in array. 0th and 1st element in each subarray represents
start/end times of an interval
"""


def merge_intervals(intervals):
        """
        :type intervals: List[List[Ints]]
        :rtype: List[List[Int]]
        """
        if not intervals:
            return []
        else:
            # sort by each element's start time
            # guaranteed end > start
            intervals.sort(key=lambda x: x[0])
            output = []

        for idx in range(1, len(intervals)):
            if intervals[idx][0] <= intervals[idx-1][1]:
                # overlap detected
                intervals[idx][0] = intervals[idx-1][0]
                intervals[idx][1] = max(intervals[idx][1], intervals[idx-1][1])

            else:
                output.append(intervals[idx-1])

        output.append(intervals[-1])  # edge case where
        return output


# test cases
assert(merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])
assert(merge_intervals([[15,18],[1,3],[8,10],[2,6]]) == [[1,6],[8,10],[15,18]])
assert(merge_intervals([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]])
assert(merge_intervals([[1,6]]) == [[1,6]])
assert(merge_intervals([[1,6],[2,6],[3,4],[3,4]]) == [[1,6]])
assert(merge_intervals([[1,4],[3,5]]) == [[1,5]])

