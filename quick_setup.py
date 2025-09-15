#!/usr/bin/env python3
"""
Quick setup script for ToneSoul System
語魂系統快速設置腳本

This script helps you get ToneSoul System up and running quickly.
此腳本幫助您快速啟動和運行語魂系統。
"""

import subprocess
import sys
import os
import platform
from pathlib import Path


def run_command(command, description, check=True):
    """Run a command with error handling"""
    print(f"\n🔄 {description}")
    print(f"   Command: {command}")
    
    try:
        if isinstance(command, str):
            result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        else:
            result = subprocess.run(command, check=check, capture_output=True, text=True)
        
        if result.stdout:
            print(f"   ✅ {result.stdout.strip()}")
        if result.stderr and check:
            print(f"   ⚠️  {result.stderr.strip()}")
        
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Failed: {e}")
        if e.stdout:
            print(f"   STDOUT: {e.stdout}")
        if e.stderr:
            print(f"   STDERR: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"   ❌ Command not found: {command}")
        return False


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("   Please install Python 3.11 or higher")
        return False


def main():
    """Main setup function"""
    print("=" * 60)
    print("🚀 ToneSoul System Quick Setup | 語魂系統快速設置")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Get project root
    project_root = Path(__file__).parent
    os.chdir(project_root)
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Detect OS
    os_name = platform.system()
    print(f"💻 Operating System: {os_name}")
    
    # Setup steps
    steps = [
        ("python -m venv venv", "Creating virtual environment | 創建虛擬環境"),
    ]
    
    # Add activation command based on OS
    if os_name == "Windows":
        steps.append(("venv\\Scripts\\activate && pip install --upgrade pip", "Activating venv and upgrading pip | 激活虛擬環境並升級 pip"))
        steps.append(("venv\\Scripts\\activate && pip install -r requirements.txt", "Installing dependencies | 安裝依賴"))
        steps.append(("venv\\Scripts\\activate && python scripts/run_tests.py", "Running tests | 運行測試"))
    else:
        steps.append(("source venv/bin/activate && pip install --upgrade pip", "Activating venv and upgrading pip | 激活虛擬環境並升級 pip"))
        steps.append(("source venv/bin/activate && pip install -r requirements.txt", "Installing dependencies | 安裝依賴"))
        steps.append(("source venv/bin/activate && python scripts/run_tests.py", "Running tests | 運行測試"))
    
    # Execute setup steps
    success_count = 0
    for command, description in steps:
        if run_command(command, description):
            success_count += 1
        else:
            print(f"\n❌ Setup failed at step: {description}")
            print("Please check the error messages above and try again.")
            return 1
    
    # Success message
    print("\n" + "=" * 60)
    print("🎉 Setup completed successfully! | 設置成功完成！")
    print("=" * 60)
    
    # Next steps
    print("\n📋 Next Steps | 下一步:")
    if os_name == "Windows":
        print("1. Activate virtual environment | 激活虛擬環境:")
        print("   venv\\Scripts\\activate")
        print("\n2. Start the server | 啟動服務器:")
        print("   python scripts/start_server.py")
    else:
        print("1. Activate virtual environment | 激活虛擬環境:")
        print("   source venv/bin/activate")
        print("\n2. Start the server | 啟動服務器:")
        print("   python scripts/start_server.py")
    
    print("\n3. Access the API documentation | 訪問 API 文檔:")
    print("   http://localhost:8000/docs")
    
    print("\n4. Test the health endpoint | 測試健康端點:")
    print("   curl http://localhost:8000/health")
    
    print("\n📚 Documentation | 文檔:")
    print("   - README.md: Project overview | 專案概述")
    print("   - docs/API.md: API documentation | API 文檔")
    print("   - docs/ARCHITECTURE.md: System architecture | 系統架構")
    print("   - DEPLOYMENT.md: Deployment guide | 部署指南")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())