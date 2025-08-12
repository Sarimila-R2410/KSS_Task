nums = list(map(int, input("Enter numbers: ").split()))

if len(nums) == len(set(nums)):
    print("All elements are unique")
else:
    print("Duplicates found")
