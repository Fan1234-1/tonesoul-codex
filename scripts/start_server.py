#!/usr/bin/env python3
"""
Server startup script for ToneSoul System
語魂系統服務器啟動腳本
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path


def main():
    """Main server startup function"""
    parser = argparse.ArgumentParser(
        description="Start ToneSoul System API Server | 啟動語魂系統 API 服務器"
    )
    parser.add_argument(
        "--host", 
        default="0.0.0.0", 
        help="Host to bind to | 綁定的主機地址"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="Port to bind to | 綁定的端口"
    )
    parser.add_argument(
        "--reload", 
        action="store_true", 
        help="Enable auto-reload for development | 啟用開發模式自動重載"
    )
    parser.add_argument(
        "--log-level", 
        default="info", 
        choices=["critical", "error", "warning", "info", "debug"],
        help="Log level | 日誌級別"
    )
    
    args = parser.parse_args()
    
    # Change to project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print("ToneSoul System API Server | 語魂系統 API 服務器")
    print("=" * 60)
    print(f"Host: {args.host}")
    print(f"Port: {args.port}")
    print(f"Reload: {args.reload}")
    print(f"Log Level: {args.log_level}")
    print(f"Working Directory: {os.getcwd()}")
    print("=" * 60)
    
    # Build uvicorn command
    command = [
        "python", "-m", "uvicorn",
        "src.main:app",
        "--host", args.host,
        "--port", str(args.port),
        "--log-level", args.log_level
    ]
    
    if args.reload:
        command.append("--reload")
    
    print(f"Starting server with command: {' '.join(command)}")
    print("\n🚀 Server starting... | 服務器啟動中...")
    print(f"📖 API Documentation: http://{args.host}:{args.port}/docs")
    print(f"🔍 ReDoc Documentation: http://{args.host}:{args.port}/redoc")
    print(f"❤️  Health Check: http://{args.host}:{args.port}/health")
    print("\nPress Ctrl+C to stop the server | 按 Ctrl+C 停止服務器")
    print("=" * 60)
    
    try:
        subprocess.run(command, check=True)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user | 服務器被用戶停止")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Server failed to start: {e}")
        return 1
    except FileNotFoundError:
        print("\n❌ uvicorn not found. Please install dependencies:")
        print("pip install -r requirements.txt")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())