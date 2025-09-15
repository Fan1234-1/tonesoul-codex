# file: tests/test_functional_modules.py
from src.core.qa_module import QAModule
from src.core.knowledge_base_module import KnowledgeBaseModule
from src.core.reflection_module import ReflectionModule
from src.core.empathy_module import EmpathyModule
from src.core.gratitude_handler_module import GratitudeHandlerModule
from src.core.complaint_handler_module import ComplaintHandlerModule
from src.core.action_executor_module import ActionExecutorModule
from src.core.assistance_module import AssistanceModule
from src.core.conversation_module import ConversationModule
from src.core.statement_processor_module import StatementProcessorModule
from src.core.default_handler_module import DefaultHandlerModule
from src.schemas.source_trace import SourceTrace, TraceStatus


def test_qa_module():
    """測試問答模組"""
    qa_module = QAModule()
    
    router_output = {
        "original_sentence": "如何學習程式設計？",
        "tone_function": "instructional",
        "source_trace": SourceTrace(id="test-qa", steps=[])
    }
    
    result = qa_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "qa_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.QAModule.v0.1"
    assert result["source_trace"].steps[0].status == TraceStatus.SUCCESS
    
    print(f"✅ QA Module test passed: {result['module_response'][:50]}...")


def test_knowledge_base_module():
    """測試知識庫模組"""
    kb_module = KnowledgeBaseModule()
    
    router_output = {
        "original_sentence": "什麼是人工智慧？",
        "tone_function": "factual_inquiry",
        "source_trace": SourceTrace(id="test-kb", steps=[])
    }
    
    result = kb_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "knowledge_base_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.KnowledgeBaseModule.v0.1"
    
    print(f"✅ Knowledge Base Module test passed: {result['module_response'][:50]}...")


def test_empathy_module():
    """測試同理心模組"""
    empathy_module = EmpathyModule()
    
    router_output = {
        "original_sentence": "我今天很難過。",
        "tone_function": "emotional_vent",
        "source_trace": SourceTrace(id="test-empathy", steps=[])
    }
    
    result = empathy_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "empathy_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.EmpathyModule.v0.1"
    
    print(f"✅ Empathy Module test passed: {result['module_response'][:50]}...")


def test_gratitude_handler_module():
    """測試感謝處理模組"""
    gratitude_module = GratitudeHandlerModule()
    
    router_output = {
        "original_sentence": "謝謝你的幫助！",
        "tone_function": "appreciation",
        "source_trace": SourceTrace(id="test-gratitude", steps=[])
    }
    
    result = gratitude_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "gratitude_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.GratitudeHandlerModule.v0.1"
    
    print(f"✅ Gratitude Handler Module test passed: {result['module_response'][:50]}...")


def test_complaint_handler_module():
    """測試抱怨處理模組"""
    complaint_module = ComplaintHandlerModule()
    
    router_output = {
        "original_sentence": "這個系統真的很糟糕。",
        "tone_function": "complaint",
        "source_trace": SourceTrace(id="test-complaint", steps=[])
    }
    
    result = complaint_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "complaint_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.ComplaintHandlerModule.v0.1"
    
    print(f"✅ Complaint Handler Module test passed: {result['module_response'][:50]}...")


def test_action_executor_module():
    """測試行動執行模組"""
    action_module = ActionExecutorModule()
    
    router_output = {
        "original_sentence": "請開啟這個檔案。",
        "tone_function": "action_request",
        "source_trace": SourceTrace(id="test-action", steps=[])
    }
    
    result = action_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "action_executed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.ActionExecutorModule.v0.1"
    
    print(f"✅ Action Executor Module test passed: {result['module_response'][:50]}...")


def test_assistance_module():
    """測試協助模組"""
    assistance_module = AssistanceModule()
    
    router_output = {
        "original_sentence": "請幫我解決這個問題。",
        "tone_function": "assistance_seeking",
        "source_trace": SourceTrace(id="test-assistance", steps=[])
    }
    
    result = assistance_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "assistance_provided"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.AssistanceModule.v0.1"
    
    print(f"✅ Assistance Module test passed: {result['module_response'][:50]}...")


def test_conversation_module():
    """測試對話模組"""
    conversation_module = ConversationModule()
    
    router_output = {
        "original_sentence": "你好，今天天氣不錯。",
        "tone_function": "casual_chat",
        "source_trace": SourceTrace(id="test-conversation", steps=[])
    }
    
    result = conversation_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "conversation_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.ConversationModule.v0.1"
    
    print(f"✅ Conversation Module test passed: {result['module_response'][:50]}...")


def test_default_handler_module():
    """測試預設處理模組"""
    default_module = DefaultHandlerModule()
    
    router_output = {
        "original_sentence": "這是一個無法分類的句子。",
        "tone_function": "unknown",
        "source_trace": SourceTrace(id="test-default", steps=[])
    }
    
    result = default_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "default_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.DefaultHandlerModule.v0.1"
    
    print(f"✅ Default Handler Module test passed: {result['module_response'][:50]}...")


def test_all_modules_error_handling():
    """測試所有模組的錯誤處理"""
    modules = [
        QAModule(), KnowledgeBaseModule(), ReflectionModule(),
        EmpathyModule(), GratitudeHandlerModule(), ComplaintHandlerModule(),
        ActionExecutorModule(), AssistanceModule(), ConversationModule(),
        StatementProcessorModule(), DefaultHandlerModule()
    ]
    
    # 測試缺少 source_trace 的情況
    invalid_input = {
        "original_sentence": "測試句子",
        "tone_function": "test"
    }
    
    for module in modules:
        try:
            module.process(invalid_input)
            assert False, f"{module.__class__.__name__} should have raised ValueError"
        except ValueError as e:
            assert "Missing source_trace" in str(e)
    
    print("✅ All modules error handling test passed")


def test_reflection_module():
    """測試反思模組"""
    reflection_module = ReflectionModule()
    
    router_output = {
        "original_sentence": "你覺得這個想法怎麼樣？",
        "tone_function": "opinion_seeking",
        "source_trace": SourceTrace(id="test-reflection", steps=[])
    }
    
    result = reflection_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "reflection_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.ReflectionModule.v0.1"
    
    print(f"✅ Reflection Module test passed: {result['module_response'][:50]}...")


def test_statement_processor_module():
    """測試陳述處理模組"""
    statement_module = StatementProcessorModule()
    
    router_output = {
        "original_sentence": "我認為這是一個好主意。",
        "tone_function": "statement_declaration",
        "source_trace": SourceTrace(id="test-statement", steps=[])
    }
    
    result = statement_module.process(router_output)
    
    assert result["module_response"] is not None
    assert result["processing_status"] == "statement_processed"
    assert len(result["source_trace"].steps) == 1
    assert result["source_trace"].steps[0].tool == "core.StatementProcessorModule.v0.1"
    
    print(f"✅ Statement Processor Module test passed: {result['module_response'][:50]}...")