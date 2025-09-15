# file: tests/test_tone_function_classifier.py
from src.core.tone_function_classifier import ToneFunctionClassifier, ToneFunction
from src.core.tone_bridge import ToneBridge
from src.schemas.source_trace import SourceTrace, TraceStep, TraceStatus


def test_classifier_vow_declaration():
    """測試承諾宣告的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "我承諾會完成這個任務。"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.VOW_DECLARATION
    assert len(result["source_trace"].steps) == 2  # ToneBridge + Classifier
    assert result["source_trace"].steps[1].tool == "core.ToneFunctionClassifier.v0.1"
    assert result["source_trace"].steps[1].status == TraceStatus.SUCCESS
    
    print(f"✅ Vow declaration test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_appreciation():
    """測試感謝表達的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "謝謝你的幫助！"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.APPRECIATION
    assert len(result["source_trace"].steps) == 2
    
    print(f"✅ Appreciation test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_instructional_question():
    """測試指導性問題的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "如何學習程式設計？"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.INSTRUCTIONAL
    assert result["intent_type"] == "question"  # 來自 ToneBridge
    
    print(f"✅ Instructional question test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_factual_inquiry():
    """測試事實性問題的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "什麼是人工智慧？"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.FACTUAL_INQUIRY
    assert result["intent_type"] == "question"
    
    print(f"✅ Factual inquiry test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_assistance_seeking():
    """測試尋求協助的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "請幫我解決這個問題。"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.ASSISTANCE_SEEKING
    
    print(f"✅ Assistance seeking test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_complaint():
    """測試抱怨表達的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "這個系統真的很糟糕。"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.COMPLAINT
    
    print(f"✅ Complaint test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_casual_chat():
    """測試閒聊的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "你好，今天天氣不錯。"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.CASUAL_CHAT
    
    print(f"✅ Casual chat test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_action_request():
    """測試行動請求的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "請開啟這個檔案。"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.ACTION_REQUEST
    assert result["intent_type"] == "request"
    
    print(f"✅ Action request test passed: '{sentence}' -> {result['tone_function']}")


def test_classifier_edge_cases():
    """測試邊界情況"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    # 測試空字串
    empty_bridge_output = {
        "intent_type": "statement",
        "original_sentence": "",
        "source_trace": SourceTrace(id="test-empty", steps=[])
    }
    result = classifier.classify(empty_bridge_output)
    assert result["tone_function"] == ToneFunction.UNKNOWN
    
    # 測試純標點符號
    punctuation_bridge_output = {
        "intent_type": "statement", 
        "original_sentence": "！！！",
        "source_trace": SourceTrace(id="test-punct", steps=[])
    }
    result = classifier.classify(punctuation_bridge_output)
    assert result["tone_function"] == ToneFunction.STATEMENT_DECLARATION
    
    print("✅ Edge cases test passed")


def test_classifier_error_handling():
    """測試錯誤處理"""
    classifier = ToneFunctionClassifier()
    
    # 測試缺少 source_trace 的情況
    invalid_input = {
        "intent_type": "statement",
        "original_sentence": "測試句子"
    }
    
    try:
        classifier.classify(invalid_input)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Missing source_trace" in str(e)
        print("✅ Error handling test passed")


def test_classifier_opinion_seeking():
    """測試尋求意見的分類"""
    classifier = ToneFunctionClassifier()
    bridge = ToneBridge()
    
    sentence = "你覺得這個想法怎麼樣？"
    bridge_output = bridge.analyze(sentence)
    result = classifier.classify(bridge_output)
    
    assert result["tone_function"] == ToneFunction.OPINION_SEEKING
    assert result["intent_type"] == "question"
    
    print(f"✅ Opinion seeking test passed: '{sentence}' -> {result['tone_function']}")


def test_full_pipeline():
    """測試完整的 ToneBridge -> ToneFunctionClassifier 流程"""
    bridge = ToneBridge()
    classifier = ToneFunctionClassifier()
    
    sentence = "我保證明天會準時完成報告。"
    
    # 第一步：ToneBridge 分析
    bridge_output = bridge.analyze(sentence)
    assert bridge_output["intent_type"] == "statement"
    assert len(bridge_output["source_trace"].steps) == 1
    
    # 第二步：ToneFunctionClassifier 分類
    final_result = classifier.classify(bridge_output)
    assert final_result["tone_function"] == ToneFunction.VOW_DECLARATION
    assert len(final_result["source_trace"].steps) == 2
    
    # 驗證追溯鏈的完整性
    steps = final_result["source_trace"].steps
    assert steps[0].tool == "core.ToneBridge.v0.1"
    assert steps[1].tool == "core.ToneFunctionClassifier.v0.1"
    assert all(step.status == TraceStatus.SUCCESS for step in steps)
    
    print(f"✅ Full pipeline test passed: '{sentence}' -> {final_result['tone_function']}")
    print(f"   Trace ID: {final_result['source_trace'].id}")
    print(f"   Steps: {len(final_result['source_trace'].steps)}")