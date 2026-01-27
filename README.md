# hello-world

这是我的第一个仓库，用于各种功能测试。

This is my first repository for various functional tests.

## 项目结构 / Project Structure

- `calculator.py` - 简单计算器模块 / Simple calculator module
- `string_utils.py` - 字符串工具函数 / String utility functions
- `test_calculator.py` - 计算器功能测试 / Calculator functional tests
- `test_string_utils.py` - 字符串工具功能测试 / String utilities functional tests

## 功能特性 / Features

### 计算器 / Calculator
- 加法 / Addition
- 减法 / Subtraction
- 乘法 / Multiplication
- 除法 / Division
- 幂运算 / Power

### 字符串工具 / String Utilities
- 字符串反转 / Reverse string
- 回文检测 / Palindrome detection
- 元音计数 / Vowel counting
- 单词首字母大写 / Capitalize words
- 移除空格 / Remove spaces

## 安装 / Installation

```bash
pip install -r requirements.txt
```

## 运行程序 / Run Programs

运行计算器演示 / Run calculator demo:
```bash
python calculator.py
```

运行字符串工具演示 / Run string utilities demo:
```bash
python string_utils.py
```

## 运行测试 / Run Tests

运行所有测试 / Run all tests:
```bash
pytest
```

运行特定测试文件 / Run specific test file:
```bash
pytest test_calculator.py
pytest test_string_utils.py
```

运行测试并显示详细信息 / Run tests with verbose output:
```bash
pytest -v
```

运行测试并显示代码覆盖率 / Run tests with coverage:
```bash
pytest --cov=. --cov-report=term-missing
```