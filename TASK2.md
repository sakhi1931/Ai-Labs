# Exercise 2 — AI-Assisted Debugging

## Task 1: Paste a buggy program and ask for diagnosis

### 1. Buggy Python Program
```python
def find_average(numbers):
    total = 0
    # Bug 1: Off-by-one error (range goes up to len(numbers) + 1)
    for i in range(len(numbers) + 1):
        total += numbrs[i]  # Bug 2: Wrong variable name 'numbrs'
    
    avg = total / len(numbers)
    # Bug 3: Missing return 
    ### 2. Diagnosis & Verification
* **Bug 1 (Off-by-one error):** `range(len(numbers) + 1)` IndexError deta hai kyunki yeh list ke size se aage chala jata hai.
* **Bug 2 (Wrong variable name):** `numbrs[i]` ki jagah `numbers[i]` aayega. Is se NameError aata hai.
* **Bug 3 (Missing return statement):** Function mein `return avg` missing hai, jisse function `None` return karta hai.

### 3. AI-Fixed Correct Code
```python
def find_average(numbers):
    if not numbers:
        return 0
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)

# Testing
print(find_average([10, 20, 30, 40]))  # Output: 25.0
---

## Task 2: Python Errors Cheat-Sheet

| Error | Simple Explanation | Common Cause | Fix Code Example |
|---|---|---|---|
| **IndexError** | Accessing an index out of list range | Incorrect loop boundary | `nums = [1, 2]; print(nums[1])` |
| **KeyError** | Searching a non-existent key in dictionary | Typo or missing key | `dict.get("key", "N/A")` |
| **TypeError** | Mismatched data types in operation | Adding String and Integer | `str(20) + " text"` |
| **RecursionError** | Function calling itself infinitely | Missing base condition | Add base case (`if n<=0: return`) |
| **AttributeError** | Calling invalid method on data type | Using append() on Int | Use correct object method |

---

## Task 3: Improve Code Quality with AI Review

### Messy Code
```python
def f(x):
    a = 0
    for i in x:
        a = a + i
    return a / len(x)
    from typing import List, Union

def calculate_average(numbers: List[Union[int, float]]) -> float:
    """Calculates the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    return sum(numbers) / len(numbers)
    def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1
    public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }
}