#!/usr/bin/env python3
"""
Test runner script for ToneSoul System
語魂系統測試運行腳本
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {description} failed")
        print(f"Return code: {e.returncode}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False


def main():
    """Main test runner"""
    print("ToneSoul System Test Runner | 語魂系統測試運行器")
    print("=" * 60)
    
    # Change to project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    print(f"Working directory: {os.getcwd()}")
    
    # Test commands to run
    test_commands = [
        ("python -m pytest tests/ -v", "Running all tests | 運行所有測試"),
        ("python -m pytest tests/test_source_trace.py -v", "Testing SourceTrace | 測試來源追溯"),
        ("python -m pytest tests/test_api.py -v", "Testing API endpoints | 測試 API 端點"),
        ("python -m pytest tests/test_functional_modules.py -v", "Testing functional modules | 測試功能模組"),
    ]
    
    # Optional: Code quality checks
    quality_commands = [
        ("python -m flake8 src/ --count --select=E9,F63,F7,F82 --show-source --statistics", 
         "Running syntax checks | 運行語法檢查"),
        ("python -c \"import src.main; print('Import test passed | 導入測試通過')\"", 
         "Testing imports | 測試導入"),
    ]
    
    success_count = 0
    total_count = 0
    
    # Run main tests
    print("\n🧪 Running Main Tests | 運行主要測試")
    for command, description in test_commands:
        total_count += 1
        if run_command(command, description):
            success_count += 1
    
    # Run quality checks
    print("\n🔍 Running Quality Checks | 運行質量檢查")
    for command, description in quality_commands:
        total_count += 1
        if run_command(command, description):
            success_count += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"TEST SUMMARY | 測試總結")
    print(f"{'='*60}")
    print(f"Passed: {success_count}/{total_count} | 通過: {success_count}/{total_count}")
    
    if success_count == total_count:
        print("✅ All tests passed! | 所有測試通過！")
        return 0
    else:
        print("❌ Some tests failed! | 部分測試失敗！")
        return 1


if __name__ == "__main__":
    sys.exit(main())