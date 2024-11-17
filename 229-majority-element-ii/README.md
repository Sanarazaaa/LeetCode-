<h2><a href="https://leetcode.com/problems/majority-element-ii">Majority Element II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an integer array of size <code>n</code>, find all elements that appear more than <code>&lfloor; n/3 &rfloor;</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> [3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?</p>

The explanation of code is the following:

Step 1: Candidate Selection
We initialize:

candidate1 = None, candidate2 = None
count1 = 0, count2 = 0
Now iterate over the array nums:

First num = 3:

Since count1 == 0, we assign:
candidate1 = 3
count1 = 1
Next num = 2:

Since num != candidate1 and count2 == 0, we assign:
candidate2 = 2
count2 = 1
Next num = 3:

Since num == candidate1, we increment:
count1 = 2
At the end of this step:

candidate1 = 3, count1 = 2
candidate2 = 2, count2 = 1
Step 2: Candidate Verification
Now verify if the candidates appear more than n // 3 times:

n = len(nums) = 3

Threshold: n // 3 = 1

nums.count(candidate1):

Counts how many times candidate1 appears in the list nums.
nums.count(candidate1) > n // 3:

Checks if the frequency of candidate1 exceeds the threshold n // 3.
result.append(candidate1):

If the condition is true, candidate1 is added to the result list because it qualifies as a majority element.
candidate2 is not None:

Ensures that candidate2 was assigned a value during the candidate selection phase. Without this check, calling nums.count(candidate2) when candidate2 is None could cause errors.
nums.count(candidate2) > n // 3:

Verifies if candidate2 appears more than n // 3 times.
result.append(candidate2):

If both conditions are true, candidate2 is added to the result list.

Variables
result:

This is a list to store the verified majority elements (elements that appear more than n // 3 times).
n = len(nums):

This calculates the total number of elements in the input list nums.
n // 3:

This represents the threshold for an element to qualify as a majority element. To be considered a majority element, the frequency of an element must exceed n // 3.
