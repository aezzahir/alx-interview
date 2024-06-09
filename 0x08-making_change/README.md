# Coin Change Problem

This repository contains a Python solution to the coin change problem using dynamic programming with optimized space complexity.

## Problem Statement

Given a list of coin denominations and a total amount, determine the fewest number of coins needed to make up that amount. If the amount cannot be made up by any combination of the coins, return -1.

## Solution Approach

The solution uses dynamic programming to solve the coin change problem efficiently. It builds a 1D dp array where `dp[i]` represents the minimum number of coins needed to make up the amount `i`. The array is initialized with infinity values, except for `dp[0]` which is set to 0 (as 0 coins are needed to make an amount of 0).

The algorithm then iterates from 1 to the total amount, and for each amount, it considers all the coin denominations. If a coin is less than or equal to the current amount, it updates `dp[i]` with the minimum of its current value and `dp[i - coin] + 1`. This step essentially considers the possibility of including the current coin in the solution.

After the iteration completes, `dp[total]` holds the minimum number of coins needed to make up the total amount. If `dp[total]` is still infinity, it means the total cannot be made up by any combination of the coins, and the function returns -1. Otherwise, it returns `dp[total]`.

## Time and Space Complexity

- Time Complexity: O(total * len(coins)), where `total` is the total amount and `len(coins)` is the number of coin denominations.
- Space Complexity: O(total), as the algorithm uses a 1D dp array of size `total + 1`.

## Usage

1. Make sure you have Python installed (version 3.4.3 or higher).
3. Navigate to the project directory: `cd coin-change-problem`
4. Run the Python script: `python3 making_change.py`

The script includes a `makeChange` function that takes a list of coin denominations and a total amount as input and returns the minimum number of coins needed to make up the total amount.

## Example

```python
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output: 3
