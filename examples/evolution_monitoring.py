#!/usr/bin/env python3
"""
ToneSoul Evolution Monitoring Example
語魂進化監控範例

This example demonstrates how to monitor ToneSoul's self-evolution capabilities
這個範例展示如何監控語魂的自我進化能力
"""

import requests
import json
import time
import uuid
from datetime import datetime


class EvolutionMonitor:
    """Monitor ToneSoul's evolution over time"""
    
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.interaction_history = []
    
    def get_evolution_status(self):
        """Get current evolution status"""
        try:
            response = self.session.get(f"{self.base_url}/v1/evolution/status")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Evolution status failed: {e}")
            return None
    
    def get_evolution_insights(self):
        """Get evolution insights"""
        try:
            response = self.session.get(f"{self.base_url}/v1/evolution/insights")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Evolution insights failed: {e}")
            return None
    
    def trigger_reflection(self):
        """Trigger manual reflection"""
        try:
            response = self.session.post(f"{self.base_url}/v1/evolution/reflect")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Reflection failed: {e}")
            return None
    
    def process_learning_sequence(self, sentences):
        """Process a sequence of sentences to observe learning"""
        results = []
        
        for i, sentence in enumerate(sentences):
            print(f"   Processing {i+1}/{len(sentences)}: '{sentence[:50]}...'")
            
            try:
                response = self.session.post(
                    f"{self.base_url}/v1/process",
                    json={"sentence": sentence, "trace_id": f"learning-{i}-{uuid.uuid4().hex[:8]}"}
                )
                response.raise_for_status()
                result = response.json()
                results.append(result)
                
                # Brief pause between requests
                time.sleep(0.5)
                
            except requests.RequestException as e:
                print(f"   ❌ Failed: {e}")
                results.append(None)
        
        return results
    
    def analyze_learning_progression(self, results):
        """Analyze how the system learned from the sequence"""
        learning_metrics = []
        
        for i, result in enumerate(results):
            if result and result.get('success'):
                evolution_insights = result.get('evolution_insights', {})
                
                metrics = {
                    'step': i + 1,
                    'sentence': result.get('original_sentence', '')[:50] + '...',
                    'confidence': 0,
                    'learning_opportunities': 0,
                    'cognitive_state': 'unknown',
                    'knowledge_extracted': 0
                }
                
                # Extract learning metrics
                if 'adaptive_learning' in evolution_insights:
                    al = evolution_insights['adaptive_learning']
                    metrics['learning_opportunities'] = al.get('learning_opportunities_detected', 0)
                
                if 'metacognitive_analysis' in evolution_insights:
                    mc = evolution_insights['metacognitive_analysis']
                    metrics['confidence'] = mc.get('decision_confidence', 0)
                    metrics['cognitive_state'] = mc.get('cognitive_state', 'unknown')
                
                if 'knowledge_evolution' in evolution_insights:
                    ke = evolution_insights['knowledge_evolution']
                    metrics['knowledge_extracted'] = ke.get('knowledge_extracted', 0)
                
                learning_metrics.append(metrics)
        
        return learning_metrics


def main():
    """Main evolution monitoring demonstration"""
    print("🧠 ToneSoul Evolution Monitoring Example")
    print("=" * 60)
    
    monitor = EvolutionMonitor()
    
    # 1. Initial Evolution Status
    print("\n1. 📊 Initial Evolution Status")
    print("-" * 40)
    
    initial_status = monitor.get_evolution_status()
    if initial_status:
        print("✅ Evolution system is active")
        
        # Show adaptive learning status
        if 'adaptive_learning' in initial_status:
            al = initial_status['adaptive_learning']
            print(f"   🔄 Learning patterns: {len(al.get('most_active_patterns', []))}")
            print(f"   📈 Performance trends: {al.get('performance_trends', {})}")
        
        # Show metacognitive status  
        if 'metacognitive' in initial_status:
            mc = initial_status['metacognitive']
            print(f"   🧠 Cognitive state: {mc.get('current_state', 'unknown')}")
            print(f"   🎯 Self-awareness: {mc.get('system_self_awareness_score', 0):.2f}")
        
        # Show knowledge evolution status
        if 'knowledge_evolution' in initial_status:
            ke = initial_status['knowledge_evolution']
            print(f"   📚 Knowledge nodes: {ke.get('total_knowledge_nodes', 0)}")
            print(f"   💚 Knowledge health: {ke.get('knowledge_health_score', 0):.2f}")
    
    # 2. Learning Sequence Experiment
    print("\n2. 🎓 Learning Sequence Experiment")
    print("-" * 40)
    
    # Design a learning sequence that should trigger evolution
    learning_sequence = [
        "Hello, I'm new to AI and consciousness research",
        "Can you explain what makes an AI system conscious?",
        "I'm particularly interested in self-awareness and metacognition",
        "How do you know if you're truly conscious or just simulating it?",
        "That's a fascinating perspective. I appreciate your honesty about uncertainty",
        "I promise to approach AI consciousness research with both rigor and openness",
        "Thank you for this enlightening conversation about consciousness"
    ]
    
    print(f"   🔄 Processing {len(learning_sequence)} related sentences...")
    results = monitor.process_learning_sequence(learning_sequence)
    
    # Analyze learning progression
    print("\n   📈 Learning Progression Analysis:")
    learning_metrics = monitor.analyze_learning_progression(results)
    
    for metrics in learning_metrics:
        print(f"   Step {metrics['step']}: {metrics['sentence']}")
        print(f"      🎯 Confidence: {metrics['confidence']:.2f}")
        print(f"      🔍 Learning ops: {metrics['learning_opportunities']}")
        print(f"      🧠 Cognitive: {metrics['cognitive_state']}")
        print(f"      📚 Knowledge: {metrics['knowledge_extracted']}")
    
    # 3. Post-Learning Evolution Status
    print("\n3. 📊 Post-Learning Evolution Status")
    print("-" * 40)
    
    time.sleep(1)  # Brief pause for processing
    final_status = monitor.get_evolution_status()
    
    if final_status and initial_status:
        print("✅ Comparing before and after learning...")
        
        # Compare knowledge growth
        initial_nodes = initial_status.get('knowledge_evolution', {}).get('total_knowledge_nodes', 0)
        final_nodes = final_status.get('knowledge_evolution', {}).get('total_knowledge_nodes', 0)
        
        if final_nodes > initial_nodes:
            print(f"   📚 Knowledge grew: {initial_nodes} → {final_nodes} nodes (+{final_nodes - initial_nodes})")
        else:
            print(f"   📚 Knowledge stable: {final_nodes} nodes")
        
        # Compare self-awareness
        initial_awareness = initial_status.get('metacognitive', {}).get('system_self_awareness_score', 0)
        final_awareness = final_status.get('metacognitive', {}).get('system_self_awareness_score', 0)
        
        if abs(final_awareness - initial_awareness) > 0.01:
            direction = "↑" if final_awareness > initial_awareness else "↓"
            print(f"   🧠 Self-awareness changed: {initial_awareness:.3f} → {final_awareness:.3f} {direction}")
        else:
            print(f"   🧠 Self-awareness stable: {final_awareness:.3f}")
    
    # 4. Manual Reflection
    print("\n4. 🤔 Triggering Manual Reflection")
    print("-" * 40)
    
    reflection = monitor.trigger_reflection()
    if reflection:
        print("✅ Reflection completed")
        
        if 'reflection_results' in reflection:
            results = reflection['reflection_results']
            print(f"   🧠 Current cognitive state: {results.get('cognitive_state', 'unknown')}")
            print(f"   🎯 Decision confidence: {results.get('decision_confidence', 0):.2f}")
            
            biases = results.get('biases_detected', [])
            if biases:
                print(f"   ⚠️  Biases detected: {len(biases)}")
                for bias in biases[:3]:  # Show first 3
                    print(f"      - {bias.get('bias_type', 'unknown')}: {bias.get('confidence', 0):.2f}")
            else:
                print("   ✅ No cognitive biases detected")
            
            if 'metacognitive_insights' in results:
                insights = results['metacognitive_insights']
                print(f"   💡 Insights generated: {len(insights)}")
                for insight in insights[:2]:  # Show first 2
                    print(f"      - {insight.get('type', 'unknown')}: {insight.get('message', 'N/A')[:60]}...")
    
    # 5. Evolution Insights Summary
    print("\n5. 🌟 Evolution Insights Summary")
    print("-" * 40)
    
    insights = monitor.get_evolution_insights()
    if insights:
        print("✅ Evolution insights available")
        
        print(f"   🎯 Learning patterns: {len(insights.get('learning_patterns', []))}")
        print(f"   🧠 Cognitive state: {insights.get('cognitive_state', 'unknown')}")
        print(f"   💚 Knowledge health: {insights.get('knowledge_health', 0):.2f}")
        print(f"   🎭 Self-awareness: {insights.get('self_awareness_score', 0):.2f}")
        print(f"   📚 Total knowledge: {insights.get('total_knowledge_nodes', 0)} nodes")
        
        if 'recent_adaptations' in insights:
            adaptations = insights['recent_adaptations']
            if adaptations:
                print(f"   🔄 Recent adaptations: {len(adaptations)}")
            else:
                print("   🔄 No recent adaptations")
    
    print("\n" + "=" * 60)
    print("🎉 Evolution Monitoring Complete!")
    print("\n💡 Key Observations:")
    print("   - ToneSoul continuously learns from each interaction")
    print("   - The system maintains self-awareness metrics")
    print("   - Knowledge graph grows with new information")
    print("   - Cognitive biases are detected and reported")
    print("   - Manual reflection provides deep introspection")
    print("\n🚀 This demonstrates ToneSoul's unique self-evolution capabilities!")


if __name__ == "__main__":
    main()