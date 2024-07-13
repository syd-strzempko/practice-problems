from collections import Counter

class Solution(object):
    def topKFrequent_raw(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        reversed_map = { value: key for (key, value) in freq_map.items()}
        # SORT is in place - cannot assign to .sort()
        reverse_list = [v for v in reversed_map.keys()]
        reverse_list.sort()
        return reversed_map[reverse_list[(k - 1)]]

    # USING A LIBRARY
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_list = Counter(nums)
        return [key for (key,v) in freq_list.most_common(k)]


x = Solution()
print(x.topKFrequent_raw([1,1,2,2,1,3], 2))

'''
# RealPython.com

from collections import defaultdict

>>> word = "mississippi"
>>> counter = defaultdict(int) # Creates dictionary with default value (int = 0) when not existing
# Eg, used as a factory function
>>> for letter in word:
...     counter[letter] += 1

## Using Counter - default hash with key, val = #

from collections import Counter

>>> # Use a string as an argument
>>> Counter("mississippi")
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

>>> # Use a list as an argument
>>> Counter(list("mississippi"))
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# can call Counter.update('more letters')
# Counter.most_common(k)
'''