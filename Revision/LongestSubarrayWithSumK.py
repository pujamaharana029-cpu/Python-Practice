def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    first_seen = {0: -1}
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        needed = prefix_sum - k

        if needed in first_seen:
            length = i - first_seen[needed]
            max_length = max(max_length, length)

        if prefix_sum not in first_seen:
            first_seen[prefix_sum] = i

    return max_length


nums = [1, -1, 5, -2, 3]
k = 3

print("Longest subarray length:", longest_subarray_sum_k(nums, k))