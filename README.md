# ToneSoul System | 語魂系統

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-red.svg)](https://pydantic.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](#english) | [中文](#中文)

---

## English

### Overview

ToneSoul System is an advanced AI processing framework that combines emotional intelligence, moral memory, and comprehensive auditability. The system processes natural language inputs through a sophisticated pipeline that includes tone analysis, function classification, strategic routing, and specialized module execution.

### Key Features

- **🎯 Tone Analysis**: Advanced sentiment and intent recognition
- **🧠 Function Classification**: Intelligent categorization of user inputs
- **🗺️ Strategic Routing**: Dynamic routing to appropriate processing modules
- **📝 Vow Management**: Moral commitment tracking and validation
- **🔍 Source Tracing**: Complete audit trail for all operations
- **⚡ FastAPI Integration**: High-performance REST API
- **🧪 Comprehensive Testing**: Full test coverage with pytest

#### 🌟 Evolution Capabilities (NEW!)
- **🔄 Adaptive Learning**: System learns from interactions and adapts behavior
- **🧠 Metacognitive Monitoring**: Self-awareness and cognitive bias detection
- **📚 Knowledge Evolution**: Dynamic knowledge graph that grows and evolves
- **🎯 Pattern Recognition**: Identifies and learns from successful processing patterns
- **🔍 Self-Reflection**: Automated system introspection and improvement
- **⚖️ Moral Framework Evolution**: Ethical decision-making that improves over time

### Architecture

```
ToneSoul System
├── Core Services
│   ├── ToneBridge (Perception)
│   ├── ToneFunctionClassifier (Understanding)
│   ├── ToneStrategicRouter (Decision)
│   └── VowChecker (Moral Memory)
├── Processing Modules
│   ├── QA Module
│   ├── Knowledge Base Module
│   ├── Reflection Module
│   ├── Empathy Module
│   ├── Gratitude Handler
│   ├── Complaint Handler
│   ├── Action Executor
│   ├── Assistance Module
│   ├── Conversation Module
│   └── Statement Processor
└── Data Schemas
    ├── SourceTrace (Audit Trail)
    └── VowObject (Moral Commitments)
```

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tonesoul-system
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API server**
   ```bash
   python src/main.py
   ```

5. **Access the API documentation**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### API Usage

#### Process a sentence
```bash
curl -X POST "http://localhost:8000/v1/process" \
     -H "Content-Type: application/json" \
     -d '{"sentence": "I promise to help you with this project"}'
```

#### Health check
```bash
curl http://localhost:8000/health
```

#### List available modules
```bash
curl http://localhost:8000/v1/modules
```

#### Evolution capabilities (NEW!)
```bash
# Get evolution status
curl http://localhost:8000/v1/evolution/status

# Get evolution insights
curl http://localhost:8000/v1/evolution/insights

# Trigger manual reflection
curl -X POST http://localhost:8000/v1/evolution/reflect
```

### Testing

Run the complete test suite:
```bash
pytest tests/ -v
```

Run specific test categories:
```bash
# API tests
pytest tests/test_api.py -v

# Core functionality tests
pytest tests/test_functional_modules.py -v

# Source trace tests
pytest tests/test_source_trace.py -v
```

### Project Structure

```
tonesoul_system/
├── src/
│   ├── core/                    # Core processing modules
│   │   ├── tone_bridge.py
│   │   ├── tone_function_classifier.py
│   │   ├── tone_strategic_router.py
│   │   ├── vow_checker.py
│   │   └── [other modules...]
│   ├── schemas/                 # Data models
│   │   ├── source_trace.py
│   │   └── vow_object.py
│   └── main.py                  # FastAPI application
├── tests/                       # Test suite
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 中文

### 概述

語魂系統是一個先進的 AI 處理框架，結合了情感智能、道德記憶和全面的可審計性。系統通過複雜的管道處理自然語言輸入，包括語調分析、功能分類、策略路由和專門的模組執行。

### 主要特性

- **🎯 語調分析**: 先進的情感和意圖識別
- **🧠 功能分類**: 智能的用戶輸入分類
- **🗺️ 策略路由**: 動態路由到適當的處理模組
- **📝 誓言管理**: 道德承諾追蹤和驗證
- **🔍 來源追溯**: 所有操作的完整審計軌跡
- **⚡ FastAPI 整合**: 高性能 REST API
- **🧪 全面測試**: 使用 pytest 的完整測試覆蓋

### 系統架構

```
語魂系統
├── 核心服務
│   ├── ToneBridge (感知)
│   ├── ToneFunctionClassifier (理解)
│   ├── ToneStrategicRouter (決策)
│   └── VowChecker (道德記憶)
├── 處理模組
│   ├── 問答模組
│   ├── 知識庫模組
│   ├── 反思模組
│   ├── 同理心模組
│   ├── 感謝處理器
│   ├── 投訴處理器
│   ├── 行動執行器
│   ├── 協助模組
│   ├── 對話模組
│   └── 語句處理器
└── 資料結構
    ├── SourceTrace (審計軌跡)
    └── VowObject (道德承諾)
```

### 快速開始

1. **克隆倉庫**
   ```bash
   git clone <repository-url>
   cd tonesoul-system
   ```

2. **設置虛擬環境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

4. **運行 API 服務器**
   ```bash
   python src/main.py
   ```

5. **訪問 API 文檔**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### API 使用

#### 處理句子
```bash
curl -X POST "http://localhost:8000/v1/process" \
     -H "Content-Type: application/json" \
     -d '{"sentence": "我承諾會幫助你完成這個專案"}'
```

#### 健康檢查
```bash
curl http://localhost:8000/health
```

#### 列出可用模組
```bash
curl http://localhost:8000/v1/modules
```

#### 進化能力 (新功能!)
```bash
# 獲取進化狀態
curl http://localhost:8000/v1/evolution/status

# 獲取進化洞察
curl http://localhost:8000/v1/evolution/insights

# 觸發手動反思
curl -X POST http://localhost:8000/v1/evolution/reflect
```

### 測試

運行完整測試套件：
```bash
pytest tests/ -v
```

運行特定測試類別：
```bash
# API 測試
pytest tests/test_api.py -v

# 核心功能測試
pytest tests/test_functional_modules.py -v

# 來源追溯測試
pytest tests/test_source_trace.py -v
```

### 專案結構

```
tonesoul_system/
├── src/
│   ├── core/                    # 核心處理模組
│   │   ├── tone_bridge.py
│   │   ├── tone_function_classifier.py
│   │   ├── tone_strategic_router.py
│   │   ├── vow_checker.py
│   │   └── [其他模組...]
│   ├── schemas/                 # 資料模型
│   │   ├── source_trace.py
│   │   └── vow_object.py
│   └── main.py                  # FastAPI 應用程式
├── tests/                       # 測試套件
├── requirements.txt             # 依賴項目
└── README.md                    # 此文件
```

### 貢獻

1. Fork 此倉庫
2. 創建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

### 授權

此專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 文件。