# file: tests/test_tone_bridge.py
from src.core.tone_bridge import ToneBridge
from src.schemas.source_trace import SourceTrace


def test_tone_bridge_analyze_question():
    """
    測試 ToneBridge 能否正確分析一個問句，並生成有效的 SourceTrace。
    """
    bridge = ToneBridge()
    sentence = "你好嗎？"
    result = bridge.analyze(sentence)
    
    # 驗證分析結果
    assert result["intent_type"] == "question"
    assert "tone_vector" in result
    
    # 驗證 SourceTrace 的生成
    assert "source_trace" in result
    source_trace = result["source_trace"]
    assert isinstance(source_trace, SourceTrace)
    assert len(source_trace.steps) == 1
    assert source_trace.steps[0].tool == "core.ToneBridge.v0.1"
    assert "Detected intent: question" in source_trace.steps[0].evidence
    
    print(f"\nTest passed for sentence: '{sentence}'")
    print(f"Generated Trace ID: {source_trace.id}")


def test_tone_bridge_analyze_statement():
    """
    測試 ToneBridge 能否正確分析一個陳述句。
    """
    bridge = ToneBridge()
    sentence = "這是一個測試。"
    result = bridge.analyze(sentence)
    
    assert result["intent_type"] == "statement"
    assert len(result["source_trace"].steps) == 1
    
    print(f"\nTest passed for sentence: '{sentence}'")
    print(f"Generated Trace ID: {result['source_trace'].id}")


def test_tone_bridge_analyze_request():
    """
    測試 ToneBridge 能否正確分析一個請求句。
    """
    bridge = ToneBridge()
    sentence = "請幫我分析這個句子。"
    result = bridge.analyze(sentence)
    
    assert result["intent_type"] == "request"
    assert len(result["source_trace"].steps) == 1
    
    print(f"\nTest passed for sentence: '{sentence}'")
    print(f"Generated Trace ID: {result['source_trace'].id}")


def test_tone_bridge_with_custom_trace_id():
    """
    測試 ToneBridge 能否使用自定義的 trace_id。
    """
    bridge = ToneBridge()
    custom_trace_id = "test-trace-123"
    sentence = "測試自定義追溯ID。"
    result = bridge.analyze(sentence, trace_id=custom_trace_id)
    
    assert result["source_trace"].id == custom_trace_id
    assert result["intent_type"] == "statement"
    
    print(f"\nTest passed with custom trace ID: {custom_trace_id}")