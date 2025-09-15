# file: tests/test_vow_checker.py
from datetime import datetime, timedelta
from src.core.vow_checker import VowChecker
from src.schemas.vow_object import VowObject, VowStatus, VowPriority
from src.schemas.source_trace import SourceTrace, TraceStatus
from src.core.tone_bridge import ToneBridge
from src.core.tone_function_classifier import ToneFunctionClassifier


def test_vow_checker_basic_commitment():
    """測試基本承諾的處理"""
    vow_checker = VowChecker()
    
    # 模擬分類器輸出
    classifier_output = {
        "original_sentence": "我承諾明天會完成這個任務。",
        "tone_function": "vow_declaration",
        "source_trace": SourceTrace(id="test-vow-basic", steps=[])
    }
    
    result = vow_checker.process_vow(classifier_output)
    
    # 驗證 VowObject 創建
    assert result["vow_object"] is not None
    vow_object = result["vow_object"]
    assert isinstance(vow_object, VowObject)
    assert vow_object.commitment == "明天會完成這個任務。"
    assert vow_object.priority == VowPriority.HIGH
    assert vow_object.status == VowStatus.ACTIVE
    assert "time_bound" in vow_object.scope
    assert "task_completion" in vow_object.scope
    
    # 驗證 SourceTrace 更新
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.VowChecker.v0.1"
    assert result["source_trace"].steps[0].status == TraceStatus.SUCCESS
    assert vow_object.id in result["source_trace"].steps[0].evidence
    
    print(f"✅ Basic commitment test passed: '{vow_object.commitment}' (ID: {vow_object.id})")


def test_vow_checker_different_keywords():
    """測試不同承諾關鍵字的處理"""
    vow_checker = VowChecker()
    
    test_cases = [
        ("我保證會準時交付。", VowPriority.HIGH, 0.9),
        ("我發誓絕不違背原則。", VowPriority.CRITICAL, 0.95),
        ("我答應幫你解決問題。", VowPriority.MEDIUM, 0.8)
    ]
    
    for sentence, expected_priority, expected_confidence in test_cases:
        classifier_output = {
            "original_sentence": sentence,
            "tone_function": "vow_declaration",
            "source_trace": SourceTrace(id=f"test-{expected_priority.value}", steps=[])
        }
        
        result = vow_checker.process_vow(classifier_output)
        vow_object = result["vow_object"]
        
        assert vow_object.priority == expected_priority
        assert vow_object.confidence_score == expected_confidence
        assert result["processing_result"] == "vow_created"
        
        print(f"✅ Keyword test passed: {expected_priority.value} priority for '{sentence}'")


def test_vow_checker_deadline_extraction():
    """測試期限提取功能"""
    vow_checker = VowChecker()
    
    test_cases = [
        ("我承諾今天完成報告。", 0),  # 今天
        ("我承諾明天提交文件。", 1),  # 明天
        ("我承諾下週開始新專案。", 7)   # 下週
    ]
    
    for sentence, expected_days in test_cases:
        classifier_output = {
            "original_sentence": sentence,
            "tone_function": "vow_declaration",
            "source_trace": SourceTrace(id=f"test-deadline-{expected_days}", steps=[])
        }
        
        result = vow_checker.process_vow(classifier_output)
        vow_object = result["vow_object"]
        
        if expected_days == 0:
            # 今天的情況
            assert vow_object.deadline is not None
            assert vow_object.deadline.date() == datetime.now().date()
        elif expected_days > 0:
            # 未來日期的情況
            assert vow_object.deadline is not None
            expected_date = datetime.now() + timedelta(days=expected_days)
            # 允許一天的誤差（因為週計算可能有差異）
            assert abs((vow_object.deadline.date() - expected_date.date()).days) <= 1
        
        print(f"✅ Deadline extraction test passed: '{sentence}' -> {vow_object.deadline}")


def test_vow_checker_scope_inference():
    """測試範圍推斷功能"""
    vow_checker = VowChecker()
    
    test_cases = [
        ("我承諾按照最高品質標準完成工作。", ["general", "task_completion", "quality_assurance"]),
        ("我承諾明天準時交付。", ["general", "time_bound", "task_completion", "quality_assurance"]),
        ("我承諾實現目標。", ["general", "task_completion"])
    ]
    
    for sentence, expected_scopes in test_cases:
        classifier_output = {
            "original_sentence": sentence,
            "tone_function": "vow_declaration",
            "source_trace": SourceTrace(id="test-scope", steps=[])
        }
        
        result = vow_checker.process_vow(classifier_output)
        vow_object = result["vow_object"]
        
        for expected_scope in expected_scopes:
            assert expected_scope in vow_object.scope
        
        print(f"✅ Scope inference test passed: '{sentence}' -> {vow_object.scope}")


def test_vow_checker_error_handling():
    """測試錯誤處理"""
    vow_checker = VowChecker()
    
    # 測試空句子
    classifier_output = {
        "original_sentence": "",
        "tone_function": "vow_declaration",
        "source_trace": SourceTrace(id="test-empty", steps=[])
    }
    
    result = vow_checker.process_vow(classifier_output)
    assert result["vow_object"] is None
    assert result["processing_result"] == "vow_creation_failed"
    assert result["source_trace"].steps[0].status == TraceStatus.FAIL
    
    # 測試沒有承諾關鍵字的句子
    classifier_output = {
        "original_sentence": "這是一個普通的句子。",
        "tone_function": "vow_declaration",
        "source_trace": SourceTrace(id="test-no-keyword", steps=[])
    }
    
    result = vow_checker.process_vow(classifier_output)
    assert result["vow_object"] is None
    assert result["processing_result"] == "vow_creation_failed"
    
    # 測試缺少 source_trace
    invalid_input = {
        "original_sentence": "我承諾完成任務。",
        "tone_function": "vow_declaration"
    }
    
    try:
        vow_checker.process_vow(invalid_input)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Missing source_trace" in str(e)
    
    print("✅ Error handling tests passed")


def test_vow_object_methods():
    """測試 VowObject 的方法"""
    vow_checker = VowChecker()
    
    classifier_output = {
        "original_sentence": "我承諾完成這個專案。",
        "tone_function": "vow_declaration",
        "source_trace": SourceTrace(id="test-methods", steps=[])
    }
    
    result = vow_checker.process_vow(classifier_output)
    vow_object = result["vow_object"]
    
    # 測試初始狀態
    assert vow_object.is_active() == True
    assert vow_object.is_expired() == False
    assert vow_object.fulfilled_at is None
    
    # 測試履行
    vow_object.fulfill()
    assert vow_object.status == VowStatus.FULFILLED
    assert vow_object.fulfilled_at is not None
    assert vow_object.is_active() == False
    
    # 測試撤回
    vow_object.withdraw()
    assert vow_object.status == VowStatus.WITHDRAWN
    
    print("✅ VowObject methods test passed")


def test_vow_checker_summary():
    """測試誓言摘要功能"""
    vow_checker = VowChecker()
    
    classifier_output = {
        "original_sentence": "我承諾明天完成報告。",
        "tone_function": "vow_declaration",
        "source_trace": SourceTrace(id="test-summary", steps=[])
    }
    
    result = vow_checker.process_vow(classifier_output)
    vow_object = result["vow_object"]
    
    summary = vow_checker.get_vow_summary(vow_object)
    
    assert summary["id"] == vow_object.id
    assert summary["commitment"] == vow_object.commitment
    assert summary["status"] == vow_object.status
    assert summary["priority"] == vow_object.priority
    assert summary["is_active"] == True
    assert summary["is_expired"] == False
    
    print(f"✅ Vow summary test passed: {summary}")


def test_full_pipeline_with_vow_checker():
    """測試完整的四模組整合流程"""
    bridge = ToneBridge()
    classifier = ToneFunctionClassifier()
    vow_checker = VowChecker()
    
    sentence = "我發誓會準時完成這個重要專案。"
    
    # 第一步：ToneBridge 分析
    bridge_output = bridge.analyze(sentence)
    assert bridge_output["intent_type"] == "statement"
    assert len(bridge_output["source_trace"].steps) == 1
    
    # 第二步：ToneFunctionClassifier 分類
    classifier_output = classifier.classify(bridge_output)
    assert classifier_output["tone_function"].value == "vow_declaration"
    assert len(classifier_output["source_trace"].steps) == 2
    
    # 第三步：VowChecker 處理
    final_result = vow_checker.process_vow(classifier_output)
    assert final_result["vow_object"] is not None
    assert final_result["processing_result"] == "vow_created"
    assert len(final_result["source_trace"].steps) == 3
    
    # 驗證完整的追溯鏈
    steps = final_result["source_trace"].steps
    assert steps[0].tool == "core.ToneBridge.v0.1"
    assert steps[1].tool == "core.ToneFunctionClassifier.v0.1"
    assert steps[2].tool == "core.VowChecker.v0.1"
    assert all(step.status == TraceStatus.SUCCESS for step in steps)
    
    # 驗證 VowObject 內容
    vow_object = final_result["vow_object"]
    assert vow_object.commitment == "會準時完成這個重要專案。"
    assert vow_object.priority == VowPriority.CRITICAL
    assert vow_object.confidence_score == 0.95
    assert "task_completion" in vow_object.scope
    assert "quality_assurance" in vow_object.scope
    
    print(f"✅ Full pipeline with VowChecker test passed:")
    print(f"   Input: '{sentence}'")
    print(f"   Vow ID: {vow_object.id}")
    print(f"   Commitment: '{vow_object.commitment}'")
    print(f"   Priority: {vow_object.priority}")
    print(f"   Scope: {vow_object.scope}")
    print(f"   Trace ID: {final_result['source_trace'].id}")
    print(f"   Total Steps: {len(final_result['source_trace'].steps)}")


def test_withdrawal_conditions():
    """測試撤回條件的設定"""
    vow_checker = VowChecker()
    
    # 測試不同優先級的撤回條件
    test_cases = [
        ("我發誓完成任務。", VowPriority.CRITICAL, "system_admin"),
        ("我承諾交付產品。", VowPriority.HIGH, "module_owner"),
        ("我答應幫忙。", VowPriority.MEDIUM, "task_owner")
    ]
    
    for sentence, expected_priority, expected_owner in test_cases:
        classifier_output = {
            "original_sentence": sentence,
            "tone_function": "vow_declaration",
            "source_trace": SourceTrace(id=f"test-withdrawal-{expected_priority.value}", steps=[])
        }
        
        result = vow_checker.process_vow(classifier_output)
        vow_object = result["vow_object"]
        
        assert vow_object.priority == expected_priority
        assert vow_object.withdrawal.repair_owner == expected_owner
        assert len(vow_object.withdrawal.conditions) > 0
        assert len(vow_object.withdrawal.repair_actions) > 0
        
        print(f"✅ Withdrawal conditions test passed: {expected_priority.value} -> {expected_owner}")
    
    print("✅ All withdrawal conditions tests passed")