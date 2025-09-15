# Contributing to ToneSoul System | 貢獻指南

[English](#english) | [中文](#中文)

---

## English

Thank you for your interest in contributing to ToneSoul System! This document provides guidelines for contributing to the project.

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/tonesoul-system.git
   cd tonesoul-system
   ```
3. **Set up the development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install development dependencies
   ```

### Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards

3. **Run tests** to ensure everything works:
   ```bash
   pytest tests/ -v
   ```

4. **Run code formatting**:
   ```bash
   black src/ tests/
   ```

5. **Run linting**:
   ```bash
   flake8 src/ tests/
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: your descriptive commit message"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request** on GitHub

### Coding Standards

- **Python Style**: Follow PEP 8 guidelines
- **Code Formatting**: Use Black for code formatting
- **Type Hints**: Use type hints for all function parameters and return values
- **Documentation**: Add docstrings for all classes and functions
- **Testing**: Write tests for new features and bug fixes

### Commit Message Guidelines

Use clear and descriptive commit messages:

- `Add: new feature or functionality`
- `Fix: bug fixes`
- `Update: changes to existing functionality`
- `Refactor: code refactoring without functionality changes`
- `Test: adding or updating tests`
- `Docs: documentation changes`

### Testing

- Write unit tests for all new functionality
- Ensure all tests pass before submitting a PR
- Aim for high test coverage
- Use descriptive test names

### Pull Request Process

1. Ensure your PR has a clear title and description
2. Reference any related issues
3. Include screenshots or examples if applicable
4. Ensure all tests pass
5. Request review from maintainers

### Reporting Issues

When reporting issues, please include:

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)
- Error messages or logs

---

## 中文

感謝您對語魂系統的貢獻興趣！本文檔提供了專案貢獻的指導原則。

### 開始使用

1. **在 GitHub 上 Fork 倉庫**
2. **本地克隆您的 fork**:
   ```bash
   git clone https://github.com/yourusername/tonesoul-system.git
   cd tonesoul-system
   ```
3. **設置開發環境**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e ".[dev]"  # 安裝開發依賴
   ```

### 開發工作流程

1. **創建功能分支**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **按照編碼標準進行更改**

3. **運行測試**確保一切正常:
   ```bash
   pytest tests/ -v
   ```

4. **運行代碼格式化**:
   ```bash
   black src/ tests/
   ```

5. **運行代碼檢查**:
   ```bash
   flake8 src/ tests/
   ```

6. **提交更改**:
   ```bash
   git add .
   git commit -m "Add: 您的描述性提交訊息"
   ```

7. **推送到您的 fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **在 GitHub 上創建 Pull Request**

### 編碼標準

- **Python 風格**: 遵循 PEP 8 指導原則
- **代碼格式化**: 使用 Black 進行代碼格式化
- **類型提示**: 為所有函數參數和返回值使用類型提示
- **文檔**: 為所有類和函數添加文檔字符串
- **測試**: 為新功能和錯誤修復編寫測試

### 提交訊息指導原則

使用清晰和描述性的提交訊息:

- `Add: 新功能或功能性`
- `Fix: 錯誤修復`
- `Update: 對現有功能的更改`
- `Refactor: 不改變功能的代碼重構`
- `Test: 添加或更新測試`
- `Docs: 文檔更改`

### 測試

- 為所有新功能編寫單元測試
- 確保在提交 PR 之前所有測試都通過
- 追求高測試覆蓋率
- 使用描述性的測試名稱

### Pull Request 流程

1. 確保您的 PR 有清晰的標題和描述
2. 引用任何相關的問題
3. 如果適用，包含截圖或示例
4. 確保所有測試通過
5. 請求維護者審查

### 報告問題

報告問題時，請包含:

- 問題的清晰描述
- 重現步驟
- 預期與實際行為
- 環境詳細信息（Python 版本、操作系統等）
- 錯誤訊息或日誌