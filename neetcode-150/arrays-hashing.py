"""
1. Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""
def hasDuplicate(self, nums: list[int]) -> bool:
    int_set = set()
    for num in nums:
        if num in int_set:
            return True
        else:
            int_set.add(num)
    return False

"""
2. Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
"""
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t): 
        return False
    
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
    
    return s_dict == t_dict

"""
3. Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
"""
def twoSum(self, nums: list[int], target: int) -> list[int]:
    num_map = {}
    for i, n in enumerate(nums):
        difference = target - n
        if difference in num_map:
            return [num_map[difference], i]
        num_map[n] = i

"""
4. Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    # schema: "key": [value]
    anagrams_dict = {}
    for item in strs:
        alphabetized_item = "".join(sorted(item))
        if alphabetized_item not in anagrams_dict:
            anagrams_dict.update({alphabetized_item: [item]})
        else:
            anagrams_dict[alphabetized_item].append(item)
    
    return [anagrams_dict[item] for item in anagrams_dict.keys()]