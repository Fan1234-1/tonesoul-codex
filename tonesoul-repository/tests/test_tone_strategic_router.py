# file: tests/test_tone_strategic_router.py
from src.core.tone_strategic_router import ToneStrategicRouter, RoutingStrategy
from src.core.tone_function_classifier import ToneFunction
from src.core.tone_bridge import ToneBridge
from src.core.tone_function_classifier import ToneFunctionClassifier
from src.schemas.source_trace import SourceTrace, TraceStep, TraceStatus


def test_router_vow_declaration():
    """測試承諾宣告的路由決策"""
    router = ToneStrategicRouter()
    
    # 模擬分類器輸出
    classifier_output = {
        "tone_function": ToneFunction.VOW_DECLARATION,
        "intent_type": "statement",
        "source_trace": SourceTrace(id="test-vow", steps=[])
    }
    
    result = router.route(classifier_output)
    
    assert result["next_strategy"]["next_module"] == "vow_checker_module"
    assert result["next_strategy"]["priority"] == "high"
    assert result["next_strategy"]["timeout_ms"] == 2000
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.ToneStrategicRouter.v0.1"
    assert result["source_trace"].steps[0].status == TraceStatus.SUCCESS
    assert "vow_checker_module" in result["source_trace"].steps[0].evidence
    
    print(f"✅ Vow declaration routing test passed: {ToneFunction.VOW_DECLARATION} -> {result['next_strategy']['next_module']}")


def test_router_instructional():
    """測試指導性問題的路由決策"""
    router = ToneStrategicRouter()
    
    classifier_output = {
        "tone_function": ToneFunction.INSTRUCTIONAL,
        "intent_type": "question",
        "source_trace": SourceTrace(id="test-instructional", steps=[])
    }
    
    result = router.route(classifier_output)
    
    assert result["next_strategy"]["next_module"] == "qa_module"
    assert result["next_strategy"]["priority"] == "high"
    assert result["next_strategy"]["timeout_ms"] == 5000
    
    print(f"✅ Instructional routing test passed: {ToneFunction.INSTRUCTIONAL} -> {result['next_strategy']['next_module']}")


def test_router_appreciation():
    """測試感謝表達的路由決策"""
    router = ToneStrategicRouter()
    
    classifier_output = {
        "tone_function": ToneFunction.APPRECIATION,
        "intent_type": "statement",
        "source_trace": SourceTrace(id="test-appreciation", steps=[])
    }
    
    result = router.route(classifier_output)
    
    assert result["next_strategy"]["next_module"] == "gratitude_handler_module"
    assert result["next_strategy"]["priority"] == "medium"
    assert result["next_strategy"]["timeout_ms"] == 1500
    
    print(f"✅ Appreciation routing test passed: {ToneFunction.APPRECIATION} -> {result['next_strategy']['next_module']}")


def test_router_complaint():
    """測試抱怨表達的路由決策"""
    router = ToneStrategicRouter()
    
    classifier_output = {
        "tone_function": ToneFunction.COMPLAINT,
        "intent_type": "statement",
        "source_trace": SourceTrace(id="test-complaint", steps=[])
    }
    
    result = router.route(classifier_output)
    
    assert result["next_strategy"]["next_module"] == "complaint_handler_module"
    assert result["next_strategy"]["priority"] == "high"
    assert result["next_strategy"]["timeout_ms"] == 3000
    
    print(f"✅ Complaint routing test passed: {ToneFunction.COMPLAINT} -> {result['next_strategy']['next_module']}")


def test_router_action_request():
    """測試行動請求的路由決策"""
    router = ToneStrategicRouter()
    
    classifier_output = {
        "tone_function": ToneFunction.ACTION_REQUEST,
        "intent_type": "request",
        "source_trace": SourceTrace(id="test-action", steps=[])
    }
    
    result = router.route(classifier_output)
    
    assert result["next_strategy"]["next_module"] == "action_executor_module"
    assert result["next_strategy"]["priority"] == "high"
    assert result["next_strategy"]["timeout_ms"] == 4000
    
    print(f"✅ Action request routing test passed: {ToneFunction.ACTION_REQUEST} -> {result['next_strategy']['next_module']}")


def test_router_fallback_strategy():
    """測試未知功能的回退策略"""
    router = ToneStrategicRouter()
    
    classifier_output = {
        "tone_function": ToneFunction.UNKNOWN,
        "intent_type": "statement",
        "source_trace": SourceTrace(id="test-unknown", steps=[])
    }
    
    result = router.route(classifier_output)
    
    assert result["next_strategy"]["next_module"] == "default_handler_module"
    assert result["next_strategy"]["priority"] == "low"
    assert result["next_strategy"]["timeout_ms"] == 2000
    assert "fallback strategy" in result["source_trace"].steps[0].evidence
    
    print(f"✅ Fallback strategy test passed: {ToneFunction.UNKNOWN} -> {result['next_strategy']['next_module']}")


def test_router_error_handling():
    """測試錯誤處理"""
    router = ToneStrategicRouter()
    
    # 測試缺少 source_trace 的情況
    invalid_input = {
        "tone_function": ToneFunction.INSTRUCTIONAL,
        "intent_type": "question"
    }
    
    try:
        router.route(invalid_input)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Missing source_trace" in str(e)
        print("✅ Error handling test passed")


def test_router_dynamic_update():
    """測試動態路由表更新"""
    router = ToneStrategicRouter()
    
    # 更新路由表
    new_strategy = RoutingStrategy(
        next_module="custom_module",
        priority="critical",
        timeout_ms=1000
    )
    router.update_routing_table(ToneFunction.CASUAL_CHAT, new_strategy)
    
    classifier_output = {
        "tone_function": ToneFunction.CASUAL_CHAT,
        "intent_type": "statement",
        "source_trace": SourceTrace(id="test-update", steps=[])
    }
    
    result = router.route(classifier_output)
    
    assert result["next_strategy"]["next_module"] == "custom_module"
    assert result["next_strategy"]["priority"] == "critical"
    assert result["next_strategy"]["timeout_ms"] == 1000
    
    print("✅ Dynamic routing table update test passed")


def test_router_get_available_routes():
    """測試獲取可用路由"""
    router = ToneStrategicRouter()
    
    routes = router.get_available_routes()
    
    # 檢查一些關鍵路由
    assert routes["vow_declaration"] == "vow_checker_module"
    assert routes["instructional"] == "qa_module"
    assert routes["appreciation"] == "gratitude_handler_module"
    assert routes["fallback"] == "default_handler_module"
    
    print(f"✅ Available routes test passed. Total routes: {len(routes)}")


def test_full_pipeline_integration():
    """測試完整的三模組整合流程"""
    bridge = ToneBridge()
    classifier = ToneFunctionClassifier()
    router = ToneStrategicRouter()
    
    sentence = "我承諾會準時完成這個專案。"
    
    # 第一步：ToneBridge 分析
    bridge_output = bridge.analyze(sentence)
    assert bridge_output["intent_type"] == "statement"
    assert len(bridge_output["source_trace"].steps) == 1
    
    # 第二步：ToneFunctionClassifier 分類
    classifier_output = classifier.classify(bridge_output)
    assert classifier_output["tone_function"] == ToneFunction.VOW_DECLARATION
    assert len(classifier_output["source_trace"].steps) == 2
    
    # 第三步：ToneStrategicRouter 路由
    final_result = router.route(classifier_output)
    assert final_result["next_strategy"]["next_module"] == "vow_checker_module"
    assert len(final_result["source_trace"].steps) == 3
    
    # 驗證完整的追溯鏈
    steps = final_result["source_trace"].steps
    assert steps[0].tool == "core.ToneBridge.v0.1"
    assert steps[1].tool == "core.ToneFunctionClassifier.v0.1"
    assert steps[2].tool == "core.ToneStrategicRouter.v0.1"
    assert all(step.status == TraceStatus.SUCCESS for step in steps)
    
    print(f"✅ Full pipeline integration test passed:")
    print(f"   Input: '{sentence}'")
    print(f"   Intent: {final_result['intent_type']}")
    print(f"   Function: {final_result['tone_function']}")
    print(f"   Next Module: {final_result['next_strategy']['next_module']}")
    print(f"   Trace ID: {final_result['source_trace'].id}")
    print(f"   Total Steps: {len(final_result['source_trace'].steps)}")


def test_all_tone_functions_routing():
    """測試所有 ToneFunction 的路由覆蓋"""
    router = ToneStrategicRouter()
    
    # 測試所有已定義的 ToneFunction
    test_functions = [
        ToneFunction.INSTRUCTIONAL,
        ToneFunction.FACTUAL_INQUIRY,
        ToneFunction.OPINION_SEEKING,
        ToneFunction.VOW_DECLARATION,
        ToneFunction.STATEMENT_DECLARATION,
        ToneFunction.EMOTIONAL_VENT,
        ToneFunction.APPRECIATION,
        ToneFunction.COMPLAINT,
        ToneFunction.ACTION_REQUEST,
        ToneFunction.ASSISTANCE_SEEKING,
        ToneFunction.CASUAL_CHAT,
        ToneFunction.UNKNOWN
    ]
    
    for tone_function in test_functions:
        classifier_output = {
            "tone_function": tone_function,
            "intent_type": "test",
            "source_trace": SourceTrace(id=f"test-{tone_function.value}", steps=[])
        }
        
        result = router.route(classifier_output)
        
        # 確保每個功能都有對應的路由
        assert "next_strategy" in result
        assert "next_module" in result["next_strategy"]
        assert result["next_strategy"]["next_module"] is not None
        
        print(f"   {tone_function.value} -> {result['next_strategy']['next_module']}")
    
    print("✅ All ToneFunction routing coverage test passed")