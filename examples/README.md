# ToneSoul Examples | 語魂範例

This directory contains practical examples demonstrating ToneSoul's capabilities.

這個目錄包含展示語魂能力的實用範例。

## 🚀 Quick Start | 快速開始

1. **Start ToneSoul server** | 啟動語魂服務器:
   ```bash
   # From project root
   python scripts/start_server.py
   ```

2. **Run examples** | 運行範例:
   ```bash
   # Run all examples
   make examples
   
   # Or run individually
   python examples/basic_usage.py
   python examples/vow_management.py
   python examples/evolution_monitoring.py
   ```

## 📚 Available Examples | 可用範例

### 1. Basic Usage (`basic_usage.py`)
**What it demonstrates** | 展示內容:
- Health checking | 健康檢查
- Basic sentence processing | 基本句子處理
- Evolution insights extraction | 進化洞察提取
- API response structure | API 響應結構

**Key features shown** | 展示的關鍵功能:
- ✅ System health monitoring
- 🧠 Intent and tone classification
- 🔄 Real-time evolution tracking
- 📊 Performance metrics

**Sample output** | 範例輸出:
```
🌟 ToneSoul System Basic Usage Example
==================================================

1. 🏥 Health Check
✅ System is healthy: healthy
   Version: 1.0.0
   Timestamp: 2025-09-15T12:00:00

2. 🧠 Basic Sentence Processing
   Input: 'Hello, how are you today?'
   ✅ Success: True
   🎯 Intent: greeting
   🎭 Function: casual_chat
   ⏱️  Latency: 150ms
   💬 Response: Hello! I'm doing well, thank you for asking...
```

### 2. Vow Management (`vow_management.py`)
**What it demonstrates** | 展示內容:
- Moral commitment detection | 道德承諾檢測
- VowObject structure and metadata | VowObject 結構和元數據
- Promise tracking and analysis | 承諾追蹤和分析
- Ethical reasoning capabilities | 倫理推理能力

**Key features shown** | 展示的關鍵功能:
- 🤝 Vow detection and classification
- 📝 Structured commitment storage
- ⏰ Deadline and scope tracking
- 🎯 Confidence scoring
- 📊 Complete audit trails

**Sample output** | 範例輸出:
```
🤝 ToneSoul Vow Management Example
==================================================

1. Time-bound commitment
   Input: 'I promise to help you complete this project by next week'
   ✅ Processed successfully
   🎯 Vow detected: Yes
   📝 Vow Details:
      ID: c50a828b-fcd6-4744-ad82-1735e98bafbf
      Commitment: help you complete this project
      Status: active
      Priority: medium
      Confidence: 0.95
```

### 3. Evolution Monitoring (`evolution_monitoring.py`)
**What it demonstrates** | 展示內容:
- Self-evolution capabilities | 自我進化能力
- Learning progression analysis | 學習進展分析
- Metacognitive monitoring | 元認知監控
- Knowledge graph growth | 知識圖譜成長

**Key features shown** | 展示的關鍵功能:
- 🧠 Cognitive state tracking
- 📈 Learning metrics analysis
- 🔄 Adaptive behavior changes
- 🤔 Self-reflection capabilities
- 📚 Knowledge evolution

**Sample output** | 範例輸出:
```
🧠 ToneSoul Evolution Monitoring Example
============================================================

1. 📊 Initial Evolution Status
✅ Evolution system is active
   🔄 Learning patterns: 3
   🧠 Cognitive state: optimal
   🎯 Self-awareness: 0.75
   📚 Knowledge nodes: 127

2. 🎓 Learning Sequence Experiment
   🔄 Processing 7 related sentences...
   📈 Learning Progression Analysis:
   Step 1: Hello, I'm new to AI and consciousness research...
      🎯 Confidence: 0.85
      🔍 Learning ops: 2
      🧠 Cognitive: learning
      📚 Knowledge: 3
```

## 🛠️ Customizing Examples | 自定義範例

### Modify Server URL | 修改服務器URL
```python
# Change the base URL if ToneSoul is running elsewhere
client = ToneSoulClient(base_url="http://your-server:8000")
```

### Add Your Own Sentences | 添加自己的句子
```python
# In basic_usage.py, modify the test_sentences list
test_sentences = [
    "Your custom sentence here",
    "Another test case",
    # ... more examples
]
```

### Create Custom Learning Sequences | 創建自定義學習序列
```python
# In evolution_monitoring.py, modify the learning_sequence
learning_sequence = [
    "First interaction to establish context",
    "Follow-up that builds on previous knowledge",
    "Complex scenario that triggers learning",
    # ... design your learning experiment
]
```

## 🔧 Troubleshooting | 故障排除

### Common Issues | 常見問題

**Connection Error** | 連接錯誤:
```
❌ Health check failed: Connection refused
```
**Solution** | 解決方案: Make sure ToneSoul server is running (`python scripts/start_server.py`)

**Import Error** | 導入錯誤:
```
ModuleNotFoundError: No module named 'requests'
```
**Solution** | 解決方案: Install dependencies (`pip install -r requirements.txt`)

**API Error** | API 錯誤:
```
❌ Processing failed: 422 Unprocessable Entity
```
**Solution** | 解決方案: Check your input format and ensure it meets API requirements

### Debug Mode | 調試模式

Run examples with debug information:
```bash
# Set debug environment variable
export TONESOUL_DEBUG=1
python examples/basic_usage.py
```

## 📊 Understanding the Output | 理解輸出

### Evolution Insights Structure | 進化洞察結構
```json
{
  "adaptive_learning": {
    "learning_opportunities_detected": 2,
    "system_performance": {...},
    "adaptation_suggestions": [...]
  },
  "metacognitive_analysis": {
    "cognitive_state": "learning",
    "decision_confidence": 0.85,
    "biases_detected": [...]
  },
  "knowledge_evolution": {
    "knowledge_extracted": 3,
    "knowledge_integrated": 2,
    "knowledge_graph_size": 127
  }
}
```

### VowObject Structure | VowObject 結構
```json
{
  "id": "uuid-string",
  "commitment": "extracted commitment text",
  "original_sentence": "full original input",
  "scope": ["context", "domain"],
  "status": "active",
  "priority": "medium",
  "confidence_score": 0.95,
  "created_at": "2025-09-15T12:00:00",
  "deadline": null
}
```

## 🎯 Next Steps | 下一步

After running these examples, you might want to:

運行這些範例後，你可能想要：

1. **Explore the API documentation** | 探索API文檔: `docs/API.md`
2. **Read about the architecture** | 閱讀架構文檔: `docs/ARCHITECTURE.md`
3. **Understand the philosophy** | 理解哲學思想: `PHILOSOPHY.md`
4. **Contribute to the project** | 為專案做貢獻: `CONTRIBUTING.md`

## 💡 Creating Your Own Examples | 創建自己的範例

Feel free to create your own examples! Here's a template:

歡迎創建自己的範例！這裡是一個模板：

```python
#!/usr/bin/env python3
"""
Your Custom ToneSoul Example
你的自定義語魂範例
"""

import requests
import json

def main():
    print("🌟 Your Custom Example")
    
    # Your code here
    # 你的代碼在這裡
    
    pass

if __name__ == "__main__":
    main()
```

---

**Happy exploring with ToneSoul! | 祝你在語魂的探索中愉快！** 🌟

*"Every interaction is an opportunity for growth and understanding."*

*"每次互動都是成長和理解的機會。"*