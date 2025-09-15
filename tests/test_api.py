# file: tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from src.main import app
import json


# 創建測試客戶端
client = TestClient(app)


def test_root_endpoint():
    """測試根端點"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["version"] == "1.0.0"
    
    print("✅ Root endpoint test passed")


def test_health_check():
    """測試健康檢查端點"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["version"] == "1.0.0"
    
    print("✅ Health check test passed")


def test_list_modules():
    """測試模組列表端點"""
    response = client.get("/v1/modules")
    assert response.status_code == 200
    data = response.json()
    assert "available_modules" in data
    assert "routing_table" in data
    assert len(data["available_modules"]) > 0
    
    print(f"✅ Modules list test passed: {len(data['available_modules'])} modules available")


def test_process_vow_declaration():
    """測試承諾宣告的完整處理流程"""
    request_data = {
        "sentence": "我承諾明天會完成這個重要任務。"
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    
    # 驗證基本響應結構
    assert data["success"] == True
    assert data["original_sentence"] == request_data["sentence"]
    assert data["intent_type"] == "statement"
    assert data["tone_function"] == "vow_declaration"
    
    # 驗證路由決策
    assert "next_strategy" in data
    assert data["next_strategy"]["next_module"] == "vow_checker_module"
    
    # 驗證 VowObject 創建
    assert data["vow_object"] is not None
    vow_object = data["vow_object"]
    assert vow_object["commitment"] == "明天會完成這個重要任務。"
    assert vow_object["priority"] == "high"
    assert vow_object["status"] == "active"
    
    # 驗證完整的追溯鏈
    assert len(data["source_trace"]) == 4  # Bridge + Classifier + Router + VowChecker
    trace_tools = [step["tool"] for step in data["source_trace"]]
    expected_tools = [
        "core.ToneBridge.v0.1",
        "core.ToneFunctionClassifier.v0.1", 
        "core.ToneStrategicRouter.v0.1",
        "core.VowChecker.v0.1"
    ]
    assert trace_tools == expected_tools
    
    # 驗證所有步驟都成功
    assert all(step["status"] == "success" for step in data["source_trace"])
    
    # 驗證性能指標
    assert data["total_latency_ms"] >= 0
    assert data["total_latency_ms"] < 5000  # 應該在 5 秒內完成
    
    print(f"✅ Vow declaration processing test passed:")
    print(f"   Trace ID: {data['trace_id']}")
    print(f"   Vow ID: {vow_object['id']}")
    print(f"   Total latency: {data['total_latency_ms']}ms")
    print(f"   Trace steps: {len(data['source_trace'])}")


def test_process_question():
    """測試問題處理流程"""
    request_data = {
        "sentence": "如何學習人工智慧？"
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    
    # 驗證基本響應
    assert data["success"] == True
    assert data["intent_type"] == "question"
    assert data["tone_function"] == "instructional"
    assert data["next_strategy"]["next_module"] == "qa_module"
    assert data["processing_status"] == "qa_processed"
    
    # 驗證模組回應
    assert "建議您可以通過以下步驟" in data["module_response"]
    
    # 驗證追溯鏈
    assert len(data["source_trace"]) == 4
    assert data["source_trace"][-1]["tool"] == "core.QAModule.v0.1"
    
    print(f"✅ Question processing test passed: {data['module_response'][:50]}...")


def test_process_gratitude():
    """測試感謝表達處理流程"""
    request_data = {
        "sentence": "謝謝你的幫助，太棒了！"
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    
    # 驗證基本響應
    assert data["success"] == True
    assert data["tone_function"] == "appreciation"
    assert data["next_strategy"]["next_module"] == "gratitude_handler_module"
    assert data["processing_status"] == "gratitude_processed"
    
    # 驗證感謝回應
    assert "不客氣" in data["module_response"] or "榮幸" in data["module_response"]
    
    print(f"✅ Gratitude processing test passed: {data['module_response'][:50]}...")


def test_process_complaint():
    """測試抱怨處理流程"""
    request_data = {
        "sentence": "這個系統真的很糟糕，我很不滿。"
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    
    # 驗證基本響應
    assert data["success"] == True
    assert data["tone_function"] == "complaint"
    assert data["next_strategy"]["next_module"] == "complaint_handler_module"
    assert data["processing_status"] == "complaint_processed"
    
    # 驗證抱怨回應
    assert "歉意" in data["module_response"] or "改善" in data["module_response"]
    
    print(f"✅ Complaint processing test passed: {data['module_response'][:50]}...")


def test_process_casual_chat():
    """測試閒聊處理流程"""
    request_data = {
        "sentence": "你好，今天天氣真不錯。"
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    
    # 驗證基本響應
    assert data["success"] == True
    assert data["tone_function"] == "casual_chat"
    assert data["next_strategy"]["next_module"] == "conversation_module"
    assert data["processing_status"] == "conversation_processed"
    
    print(f"✅ Casual chat processing test passed: {data['module_response'][:50]}...")


def test_process_with_custom_trace_id():
    """測試使用自定義追溯 ID"""
    custom_trace_id = "test-trace-12345"
    request_data = {
        "sentence": "我答應會準時完成。",
        "trace_id": custom_trace_id
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["success"] == True
    assert data["trace_id"] == custom_trace_id
    
    print(f"✅ Custom trace ID test passed: {custom_trace_id}")


def test_process_empty_sentence():
    """測試空句子的錯誤處理"""
    request_data = {
        "sentence": ""
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 422  # Validation error
    
    print("✅ Empty sentence validation test passed")


def test_process_very_long_sentence():
    """測試超長句子的處理"""
    long_sentence = "這是一個很長的句子。" * 100  # 超過 500 字符
    request_data = {
        "sentence": long_sentence
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 422  # Validation error
    
    print("✅ Long sentence validation test passed")


def test_process_unknown_function():
    """測試無法分類的句子（回退到預設處理）"""
    request_data = {
        "sentence": "這是一個很奇怪的句子，包含一些無法分類的內容。"
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["success"] == True
    
    # 可能會被分類為 statement_declaration 或 unknown
    assert data["tone_function"] in ["statement_declaration", "unknown"]
    
    print(f"✅ Unknown function processing test passed: {data['tone_function']}")


def test_multiple_requests_performance():
    """測試多個請求的性能"""
    test_sentences = [
        "我承諾完成任務。",
        "如何學習程式設計？",
        "謝謝你的幫助。",
        "你好，天氣不錯。",
        "這個系統有問題。"
    ]
    
    total_latency = 0
    successful_requests = 0
    
    for sentence in test_sentences:
        request_data = {"sentence": sentence}
        response = client.post("/v1/process", json=request_data)
        
        if response.status_code == 200:
            data = response.json()
            if data["success"]:
                total_latency += data["total_latency_ms"]
                successful_requests += 1
    
    assert successful_requests == len(test_sentences)
    average_latency = total_latency / successful_requests
    
    print(f"✅ Performance test passed:")
    print(f"   Successful requests: {successful_requests}/{len(test_sentences)}")
    print(f"   Average latency: {average_latency:.2f}ms")
    print(f"   Total latency: {total_latency}ms")


def test_api_response_structure():
    """測試 API 響應結構的完整性"""
    request_data = {
        "sentence": "我保證會做好這件事。"
    }
    
    response = client.post("/v1/process", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    
    # 驗證所有必需的字段都存在
    required_fields = [
        "success", "trace_id", "original_sentence", "intent_type",
        "tone_function", "next_strategy", "module_response",
        "processing_status", "source_trace", "total_latency_ms"
    ]
    
    for field in required_fields:
        assert field in data, f"Missing required field: {field}"
    
    # 驗證 source_trace 結構
    for step in data["source_trace"]:
        step_fields = ["tool", "status", "evidence", "trust_level", "latency_ms", "timestamp"]
        for field in step_fields:
            assert field in step, f"Missing trace step field: {field}"
    
    print("✅ API response structure test passed")


def test_concurrent_requests():
    """測試並發請求處理"""
    import threading
    import time
    
    results = []
    
    def make_request(sentence_id):
        request_data = {"sentence": f"測試並發請求 {sentence_id}"}
        response = client.post("/v1/process", json=request_data)
        results.append({
            "id": sentence_id,
            "status_code": response.status_code,
            "success": response.json().get("success", False) if response.status_code == 200 else False
        })
    
    # 創建 5 個並發請求
    threads = []
    for i in range(5):
        thread = threading.Thread(target=make_request, args=(i,))
        threads.append(thread)
        thread.start()
    
    # 等待所有線程完成
    for thread in threads:
        thread.join()
    
    # 驗證結果
    assert len(results) == 5
    successful_requests = sum(1 for r in results if r["success"])
    assert successful_requests == 5
    
    print(f"✅ Concurrent requests test passed: {successful_requests}/5 successful")