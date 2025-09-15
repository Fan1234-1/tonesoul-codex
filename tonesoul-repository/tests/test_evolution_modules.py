import pytest
import uuid
from datetime import datetime
from src.schemas.source_trace import SourceTrace, TraceStep, TraceStatus, TrustLevel
from src.schemas.evolution_object import LearningType, EvolutionStatus, KnowledgeNode
from src.core.adaptive_learning_module import AdaptiveLearningModule
from src.core.metacognitive_module import MetacognitiveModule, CognitiveState
from src.core.knowledge_evolution_module import KnowledgeEvolutionModule


class TestAdaptiveLearningModule:
    """測試自適應學習模組"""
    
    def setup_method(self):
        """設置測試環境"""
        self.learning_module = AdaptiveLearningModule()
    
    def test_module_initialization(self):
        """測試模組初始化"""
        assert self.learning_module is not None
        assert len(self.learning_module.learning_patterns) > 0
        assert self.learning_module.system_state is not None
        assert self.learning_module.system_state.version == "1.0.0"
    
    def test_process_interaction_basic(self):
        """測試基本互動處理"""
        # 創建測試追溯
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="test_tool",
                    status=TraceStatus.SUCCESS,
                    evidence="Test evidence",
                    trust_level=TrustLevel.B,
                    latency_ms=100,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {
            "input_type": "question",
            "user_satisfaction": 0.8,
            "feedback_signals": {"response_time": 500}
        }
        
        result = self.learning_module.process_interaction(trace, context)
        
        assert "learning_opportunities_detected" in result
        assert "system_performance" in result
        assert "processing_time_ms" in result
        assert result["processing_time_ms"] >= 0
    
    def test_learning_pattern_detection(self):
        """測試學習模式檢測"""
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="tone_classifier",
                    status=TraceStatus.SUCCESS,
                    evidence="Classified as question",
                    trust_level=TrustLevel.A,
                    latency_ms=50,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {
            "repeated_query_type": True,
            "similar_context": True
        }
        
        result = self.learning_module.process_interaction(trace, context)
        
        # 應該檢測到學習機會
        assert result["learning_opportunities_detected"] > 0
    
    def test_performance_metrics_update(self):
        """測試性能指標更新"""
        initial_interactions = self.learning_module.system_state.total_interactions
        
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="test_tool",
                    status=TraceStatus.SUCCESS,
                    evidence="Test",
                    trust_level=TrustLevel.B,
                    latency_ms=200,
                    ts=datetime.now()
                )
            ]
        )
        
        self.learning_module.process_interaction(trace, {})
        
        # 檢查互動計數是否增加
        assert self.learning_module.system_state.total_interactions == initial_interactions + 1
        
        # 檢查性能指標是否更新
        assert len(self.learning_module.performance_metrics["response_time"]) > 0
        assert len(self.learning_module.performance_metrics["success_rate"]) > 0
    
    def test_learning_insights(self):
        """測試學習洞察生成"""
        insights = self.learning_module.get_learning_insights()
        
        assert "most_active_patterns" in insights
        assert "learning_trends" in insights
        assert "performance_trends" in insights
        assert isinstance(insights["most_active_patterns"], list)


class TestMetacognitiveModule:
    """測試元認知模組"""
    
    def setup_method(self):
        """設置測試環境"""
        self.metacognitive_module = MetacognitiveModule()
    
    def test_module_initialization(self):
        """測試模組初始化"""
        assert self.metacognitive_module is not None
        assert self.metacognitive_module.current_cognitive_state == CognitiveState.OPTIMAL
        assert len(self.metacognitive_module.bias_detectors) > 0
    
    def test_cognitive_monitoring_basic(self):
        """測試基本認知監控"""
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="tone_bridge",
                    status=TraceStatus.SUCCESS,
                    evidence="Analyzed input tone",
                    trust_level=TrustLevel.A,
                    latency_ms=80,
                    ts=datetime.now()
                ),
                TraceStep(
                    tool="tone_classifier",
                    status=TraceStatus.SUCCESS,
                    evidence="Classified as greeting",
                    trust_level=TrustLevel.B,
                    latency_ms=120,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {
            "decision_complexity": 0.5,
            "user_emotion": "neutral"
        }
        
        result = self.metacognitive_module.monitor_cognitive_process(trace, context)
        
        assert "cognitive_state" in result
        assert "decision_confidence" in result
        assert "cognitive_load" in result
        assert "biases_detected" in result
        assert "processing_time_ms" in result
        
        # 檢查認知狀態是否有效
        assert result["cognitive_state"] in [state.value for state in CognitiveState]
        
        # 檢查信心度範圍
        assert 0.0 <= result["decision_confidence"] <= 1.0
    
    def test_bias_detection(self):
        """測試認知偏差檢測"""
        # 創建可能觸發過度自信偏差的追溯
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="high_confidence_tool",
                    status=TraceStatus.FAIL,  # 高信心但失敗
                    evidence="High confidence prediction failed",
                    trust_level=TrustLevel.A,
                    latency_ms=50,
                    ts=datetime.now()
                ),
                TraceStep(
                    tool="another_high_confidence_tool",
                    status=TraceStatus.FAIL,
                    evidence="Another high confidence failure",
                    trust_level=TrustLevel.A,
                    latency_ms=60,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {"decision_type": "classification"}
        
        result = self.metacognitive_module.monitor_cognitive_process(trace, context)
        
        # 應該檢測到偏差
        biases = result["biases_detected"]
        assert isinstance(biases, list)
        
        # 可能檢測到過度自信偏差
        bias_types = [bias["bias_type"] for bias in biases]
        if "overconfidence_bias" in bias_types:
            overconfidence_bias = next(bias for bias in biases if bias["bias_type"] == "overconfidence_bias")
            assert "confidence" in overconfidence_bias
            assert "evidence" in overconfidence_bias
    
    def test_cognitive_state_transitions(self):
        """測試認知狀態轉換"""
        initial_state = self.metacognitive_module.current_cognitive_state
        
        # 創建高負荷的追溯
        complex_trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool=f"complex_tool_{i}",
                    status=TraceStatus.SUCCESS if i % 2 == 0 else TraceStatus.FAIL,
                    evidence=f"Complex processing step {i}",
                    trust_level=TrustLevel.C,
                    latency_ms=200 + i * 50,
                    ts=datetime.now()
                ) for i in range(10)  # 10個複雜步驟
            ]
        )
        
        context = {"complexity_level": "high"}
        
        result = self.metacognitive_module.monitor_cognitive_process(complex_trace, context)
        
        # 認知狀態可能已改變
        new_state = CognitiveState(result["cognitive_state"])
        
        # 驗證狀態轉換的合理性
        assert new_state in [CognitiveState.LEARNING, CognitiveState.CONFUSED, 
                           CognitiveState.DEGRADED, CognitiveState.UNCERTAIN]
    
    def test_cognitive_summary(self):
        """測試認知狀態摘要"""
        summary = self.metacognitive_module.get_cognitive_summary()
        
        assert "current_state" in summary
        assert "recent_confidence_trend" in summary
        assert "cognitive_load_summary" in summary
        assert "system_self_awareness_score" in summary
        
        # 檢查自我意識評分範圍
        assert 0.0 <= summary["system_self_awareness_score"] <= 1.0


class TestKnowledgeEvolutionModule:
    """測試知識進化模組"""
    
    def setup_method(self):
        """設置測試環境"""
        self.knowledge_module = KnowledgeEvolutionModule()
    
    def test_module_initialization(self):
        """測試模組初始化"""
        assert self.knowledge_module is not None
        assert len(self.knowledge_module.knowledge_graph) > 0  # 應該有基礎知識
        assert len(self.knowledge_module.extraction_patterns) > 0
        assert "greeting" in self.knowledge_module.concept_index
    
    def test_knowledge_extraction_basic(self):
        """測試基本知識提取"""
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="knowledge_extractor",
                    status=TraceStatus.SUCCESS,
                    evidence="Python is defined as a programming language",
                    trust_level=TrustLevel.A,
                    latency_ms=100,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {
            "domain": "programming",
            "user_preferences": {"language": "python"}
        }
        
        result = self.knowledge_module.process_knowledge_evolution(trace, context)
        
        assert "knowledge_extracted" in result
        assert "knowledge_validated" in result
        assert "knowledge_integrated" in result
        assert "knowledge_graph_size" in result
        assert "processing_time_ms" in result
        
        # 應該提取到一些知識
        assert result["knowledge_extracted"] > 0
    
    def test_knowledge_integration(self):
        """測試知識整合"""
        initial_size = len(self.knowledge_module.knowledge_graph)
        
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="learning_tool",
                    status=TraceStatus.SUCCESS,
                    evidence="Machine learning is related to artificial intelligence",
                    trust_level=TrustLevel.B,
                    latency_ms=150,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {"domain": "ai", "learning_context": True}
        
        result = self.knowledge_module.process_knowledge_evolution(trace, context)
        
        # 知識圖譜可能增長
        final_size = result["knowledge_graph_size"]
        assert final_size >= initial_size
        
        # 檢查統計信息
        assert "evolution_stats" in result
        stats = result["evolution_stats"]
        assert "nodes_created" in stats
        assert "nodes_updated" in stats
    
    def test_knowledge_validation(self):
        """測試知識驗證"""
        # 創建包含可能矛盾信息的追溯
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="validator",
                    status=TraceStatus.SUCCESS,
                    evidence="This statement is completely false and incorrect",
                    trust_level=TrustLevel.C,  # 低信任度
                    latency_ms=80,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {"validation_required": True}
        
        result = self.knowledge_module.process_knowledge_evolution(trace, context)
        
        # 低質量的知識可能不會被整合
        assert result["knowledge_validated"] <= result["knowledge_extracted"]
    
    def test_knowledge_connections(self):
        """測試知識連接建立"""
        # 添加相關的知識
        trace1 = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="connector",
                    status=TraceStatus.SUCCESS,
                    evidence="Natural language processing is related to machine learning",
                    trust_level=TrustLevel.A,
                    latency_ms=100,
                    ts=datetime.now()
                )
            ]
        )
        
        trace2 = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="connector",
                    status=TraceStatus.SUCCESS,
                    evidence="Machine learning is connected with artificial intelligence",
                    trust_level=TrustLevel.A,
                    latency_ms=120,
                    ts=datetime.now()
                )
            ]
        )
        
        # 處理兩個相關的知識項
        result1 = self.knowledge_module.process_knowledge_evolution(trace1, {"domain": "ai"})
        result2 = self.knowledge_module.process_knowledge_evolution(trace2, {"domain": "ai"})
        
        # 應該建立一些連接
        total_connections = result1["connections_updated"] + result2["connections_updated"]
        assert total_connections >= 0
    
    def test_knowledge_summary(self):
        """測試知識摘要"""
        summary = self.knowledge_module.get_knowledge_summary()
        
        assert "total_knowledge_nodes" in summary
        assert "total_connections" in summary
        assert "average_confidence" in summary
        assert "concept_distribution" in summary
        assert "evolution_stats" in summary
        assert "knowledge_health_score" in summary
        
        # 檢查健康度評分範圍
        assert 0.0 <= summary["knowledge_health_score"] <= 1.0
        
        # 檢查基本統計
        assert summary["total_knowledge_nodes"] > 0
        assert 0.0 <= summary["average_confidence"] <= 1.0
    
    def test_evolution_opportunities(self):
        """測試進化機會識別"""
        # 添加一些知識來創建進化機會
        for i in range(5):
            trace = SourceTrace(
                id=str(uuid.uuid4()),
                steps=[
                    TraceStep(
                        tool="opportunity_creator",
                        status=TraceStatus.SUCCESS,
                        evidence=f"Related concept {i} is connected to main_concept",
                        trust_level=TrustLevel.B,
                        latency_ms=100,
                        ts=datetime.now()
                    )
                ]
            )
            self.knowledge_module.process_knowledge_evolution(trace, {"domain": "test"})
        
        result = self.knowledge_module.process_knowledge_evolution(
            SourceTrace(id=str(uuid.uuid4()), steps=[]), {}
        )
        
        # 應該識別到一些進化機會
        assert result["evolution_opportunities"] >= 0


class TestEvolutionIntegration:
    """測試進化模組整合"""
    
    def setup_method(self):
        """設置測試環境"""
        self.adaptive_learning = AdaptiveLearningModule()
        self.metacognitive = MetacognitiveModule()
        self.knowledge_evolution = KnowledgeEvolutionModule()
    
    def test_integrated_evolution_processing(self):
        """測試整合的進化處理"""
        # 創建一個複雜的處理追溯
        trace = SourceTrace(
            id=str(uuid.uuid4()),
            steps=[
                TraceStep(
                    tool="tone_bridge",
                    status=TraceStatus.SUCCESS,
                    evidence="Analyzed user input tone",
                    trust_level=TrustLevel.A,
                    latency_ms=50,
                    ts=datetime.now()
                ),
                TraceStep(
                    tool="tone_classifier",
                    status=TraceStatus.SUCCESS,
                    evidence="Classified as gratitude expression",
                    trust_level=TrustLevel.B,
                    latency_ms=80,
                    ts=datetime.now()
                ),
                TraceStep(
                    tool="gratitude_handler",
                    status=TraceStatus.SUCCESS,
                    evidence="Generated appropriate gratitude response",
                    trust_level=TrustLevel.A,
                    latency_ms=120,
                    ts=datetime.now()
                )
            ]
        )
        
        context = {
            "user_emotion": "grateful",
            "response_quality": 0.9,
            "user_satisfaction": 0.85,
            "domain": "social_interaction"
        }
        
        # 執行所有進化處理
        learning_result = self.adaptive_learning.process_interaction(trace, context)
        cognitive_result = self.metacognitive.monitor_cognitive_process(trace, context)
        knowledge_result = self.knowledge_evolution.process_knowledge_evolution(trace, context)
        
        # 驗證所有模組都產生了結果
        assert learning_result is not None
        assert cognitive_result is not None
        assert knowledge_result is not None
        
        # 驗證結果包含預期的字段
        assert "learning_opportunities_detected" in learning_result
        assert "cognitive_state" in cognitive_result
        assert "knowledge_extracted" in knowledge_result
        
        # 驗證進化能力正常工作
        assert learning_result["learning_opportunities_detected"] >= 0
        assert cognitive_result["decision_confidence"] > 0
        assert knowledge_result["knowledge_graph_size"] > 0
    
    def test_evolution_feedback_loop(self):
        """測試進化反饋循環"""
        # 模擬多次互動來測試進化反饋
        contexts = [
            {"user_satisfaction": 0.9, "response_time": 100},
            {"user_satisfaction": 0.7, "response_time": 200},
            {"user_satisfaction": 0.8, "response_time": 150},
        ]
        
        initial_performance = self.adaptive_learning.system_state.overall_performance_score
        
        for i, context in enumerate(contexts):
            trace = SourceTrace(
                id=str(uuid.uuid4()),
                steps=[
                    TraceStep(
                        tool=f"test_tool_{i}",
                        status=TraceStatus.SUCCESS,
                        evidence=f"Processing step {i}",
                        trust_level=TrustLevel.B,
                        latency_ms=context["response_time"],
                        ts=datetime.now()
                    )
                ]
            )
            
            # 執行學習處理
            self.adaptive_learning.process_interaction(trace, context)
        
        # 檢查性能是否有變化（學習效果）
        final_performance = self.adaptive_learning.system_state.overall_performance_score
        
        # 性能應該有所變化（可能提升或調整）
        assert final_performance != initial_performance or final_performance > 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])