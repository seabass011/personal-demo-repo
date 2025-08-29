# 🚀 Nova CI-Rescue Demo Repository

A demo repository to test **Nova CI-Rescue's automatic test fixing capabilities**.

## 🎯 What This Demo Does

- ✅ Contains a simple calculator module with **intentional bugs**
- ✅ Includes comprehensive tests that will **initially fail**
- ✅ Has a GitHub Actions workflow for CI
- ✅ Perfect for testing Nova's ability to fix failing tests

## 🧪 Current Status

**Tests will FAIL initially** due to these intentional bugs:

- ❌ Division by zero not handled
- ❌ Negative square roots not handled
- ❌ Factorial for negative numbers not handled
- ❌ Fibonacci for negative numbers (infinite recursion)
- ❌ Average of empty list (division by zero)

## 🚀 How to Test Nova CI-Rescue

### Step 1: Install Nova on This Repository

**Option A: One-Click Installation (Recommended)**

1. Visit: https://nova-ci-rescue.fly.dev/setup
2. Click "Install Nova CI-Rescue"
3. Select this repository: `seabass011/nova-ci-rescue-demo`
4. Complete the GitHub OAuth flow

**Option B: Manual Installation**

1. Go to https://github.com/settings/apps
2. Find "Nova CI-Rescue" app
3. Install it on this repository

### Step 2: Push Code to Trigger CI

```bash
# Push the current code (tests will fail)
git add .
git commit -m "Add demo with intentional bugs"
git push origin main
```

### Step 3: Watch Nova Work Its Magic! ✨

Nova will automatically:

1. 🔍 **Detect** the failing CI build
2. 🧠 **Analyze** the test failures and code
3. 🛠️ **Generate** fixes for the bugs
4. 🌿 **Create** a new branch with the fixes
5. 📝 **Open** a pull request with the solution
6. 👥 **Add** you as a reviewer

### Step 4: Review Nova's PR

Nova will create a PR like:

```
Title: Fix calculator bugs and add error handling

Description:
- Fixed division by zero in divide() function
- Added negative number validation for square_root()
- Fixed factorial for negative numbers
- Added empty list check for average()
- All tests now passing ✅

Files changed:
- calculator.py: Added proper error handling
- test_calculator.py: Enhanced test coverage
```

## 📁 Project Structure

```
nova-ci-rescue-demo/
├── calculator.py          # Calculator module with intentional bugs
├── test_calculator.py     # Comprehensive test suite
├── requirements.txt       # Python dependencies
├── .nova-ci-rescue.yml    # Nova configuration
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI workflow
└── README.md             # This file
```

## 🐛 Intentional Bugs (For Testing)

The `calculator.py` contains these bugs that Nova should fix:

```python
# Division by zero not handled
def divide(a, b):
    return a / b  # Will crash on divide(10, 0)

# Negative square root not handled
def square_root(a):
    return a ** 0.5  # Will return complex number for negative

# Factorial for negative numbers not handled
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # Will cause infinite recursion

# Empty list average not handled
def average(numbers):
    return sum(numbers) / len(numbers)  # Will crash on average([])
```

## 🔧 Nova Configuration

The `.nova-ci-rescue.yml` file configures Nova's behavior:

```yaml
max_iters: 5 # Maximum fix attempts
language: python # Programming language
paths:
  include: ["calculator.py"] # Only fix these files
  exclude: [".github/**"] # Don't touch these
```

## 🎯 Expected Nova Behavior

When you push this code, Nova should:

1. **Monitor** GitHub Actions CI status
2. **Detect** test failures
3. **Analyze** the error messages and code
4. **Generate** fixes like:
   ```python
   def divide(a, b):
       if b == 0:
           raise ValueError("Cannot divide by zero")
       return a / b
   ```
5. **Test** the fixes internally
6. **Create** a new branch and PR
7. **Add** you as reviewer

## 📊 Test Results

**Initial (Failing) Tests:**

```bash
$ pytest test_calculator.py -v
======================== FAILURES ========================
FAILED test_calculator.py::TestDivision::test_divide_by_zero
FAILED test_calculator.py::TestSquareRoot::test_square_root_negative
FAILED test_calculator.py::TestFactorial::test_factorial_negative
FAILED test_calculator.py::TestFibonacci::test_fibonacci_negative
FAILED test_calculator.py::TestAverage::test_average_empty_list
================ 5 failed, 15 passed ================
```

**After Nova's Fix (Expected):**

```bash
$ pytest test_calculator.py -v
======================== SUCCESS ========================
16 passed, 0 failed
```

## 🌟 Try It Now!

1. **Push this code** to trigger CI failures
2. **Watch Nova** automatically create fixes
3. **Review the PR** Nova opens
4. **Merge** Nova's perfect fix!

---

**Built with ❤️ for testing Nova CI-Rescue**
