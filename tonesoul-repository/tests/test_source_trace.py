import uuid
from datetime import datetime
from src.schemas.source_trace import SourceTrace, TraceStep, TraceStatus, TrustLevel


def test_create_source_trace_successfully():
    """
    測試 SourceTrace 物件能否被成功創建並包含有效的步驟。
    """
    trace_id = str(uuid.uuid4())
    now = datetime.now()
    
    step1 = TraceStep(
        tool="self.input_parser",
        status=TraceStatus.SUCCESS,
        input_digest="sha256-abc...",
        evidence="User provided 4 files.",
        trust_level=TrustLevel.C,
        latency_ms=150,
        ts=now
    )
    
    step2 = TraceStep(
        tool="self.reflection_engine",
        status=TraceStatus.SUCCESS,
        evidence="Synthesized user's philosophy into three pillars.",
        trust_level=TrustLevel.C,
        latency_ms=1200,
        ts=now
    )
    
    source_trace = SourceTrace(id=trace_id, steps=[step1, step2])
    
    # 驗證核心屬性
    assert source_trace.id == trace_id
    assert len(source_trace.steps) == 2
    assert source_trace.steps[0].tool == "self.input_parser"
    assert source_trace.steps[1].trust_level == TrustLevel.C
    assert source_trace.steps[0].status == "success"
    
    # 驗證 Pydantic 的模型序列化功能
    json_output = source_trace.model_dump_json(indent=2)
    assert trace_id in json_output
    print("\nSourceTrace JSON output:\n", json_output)


def test_json_serialization_validation():
    """
    測試 JSON 序列化功能，驗證所有欄位都正確序列化。
    """
    trace_id = str(uuid.uuid4())
    now = datetime.now()
    
    step = TraceStep(
        tool="web.search",
        status=TraceStatus.SUCCESS,
        input_digest="sha256-def456",
        evidence="Found 5 relevant documents",
        trust_level=TrustLevel.A,
        latency_ms=2500,
        ts=now
    )
    
    source_trace = SourceTrace(id=trace_id, steps=[step])
    
    # 測試 JSON 序列化
    json_output = source_trace.model_dump_json(indent=2)
    
    # 驗證 JSON 包含所有必要欄位
    assert trace_id in json_output
    assert "web.search" in json_output
    assert "success" in json_output
    assert "sha256-def456" in json_output
    assert "Found 5 relevant documents" in json_output
    assert '"A"' in json_output  # TrustLevel.A
    assert "2500" in json_output  # latency_ms
    
    # 驗證 datetime 正確序列化
    assert now.isoformat() in json_output or now.strftime("%Y-%m-%d") in json_output
    
    print(f"\nJSON serialization test passed. Output length: {len(json_output)} characters")


def test_data_validation_and_error_handling():
    """
    測試資料驗證和錯誤處理功能。
    """
    import pytest
    from pydantic import ValidationError
    
    # 測試必填欄位驗證
    with pytest.raises(ValidationError) as exc_info:
        TraceStep()  # 沒有提供任何必填欄位
    
    assert "Field required" in str(exc_info.value)
    
    # 測試無效的 TraceStatus
    with pytest.raises(ValidationError) as exc_info:
        TraceStep(
            tool="test_tool",
            status="invalid_status",  # 無效的狀態
            evidence="test evidence",
            trust_level=TrustLevel.A,
            latency_ms=100,
            ts=datetime.now()
        )
    
    # 測試無效的 TrustLevel
    with pytest.raises(ValidationError) as exc_info:
        TraceStep(
            tool="test_tool",
            status=TraceStatus.SUCCESS,
            evidence="test evidence",
            trust_level="D",  # 無效的信任等級
            latency_ms=100,
            ts=datetime.now()
        )
    
    # 測試無效的資料類型
    with pytest.raises(ValidationError) as exc_info:
        TraceStep(
            tool="test_tool",
            status=TraceStatus.SUCCESS,
            evidence="test evidence",
            trust_level=TrustLevel.A,
            latency_ms="not_an_integer",  # 應該是整數
            ts=datetime.now()
        )
    
    print("Data validation tests passed successfully!")