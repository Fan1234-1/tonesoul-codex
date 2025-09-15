#!/usr/bin/env python3
"""
ToneSoul System Basic Usage Example
語魂系統基本使用範例

This example demonstrates how to interact with the ToneSoul API
這個範例展示如何與語魂API互動
"""

import requests
import json
import time
from datetime import datetime


class ToneSoulClient:
    """Simple client for ToneSoul API"""
    
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def health_check(self):
        """Check if ToneSoul is running"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Health check failed: {e}")
            return None
    
    def process_sentence(self, sentence, trace_id=None):
        """Process a sentence through ToneSoul"""
        payload = {"sentence": sentence}
        if trace_id:
            payload["trace_id"] = trace_id
        
        try:
            response = self.session.post(
                f"{self.base_url}/v1/process",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Processing failed: {e}")
            return None
    
    def get_evolution_status(self):
        """Get system evolution status"""
        try:
            response = self.session.get(f"{self.base_url}/v1/evolution/status")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Evolution status failed: {e}")
            return None
    
    def trigger_reflection(self):
        """Trigger manual system reflection"""
        try:
            response = self.session.post(f"{self.base_url}/v1/evolution/reflect")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Reflection failed: {e}")
            return None


def main():
    """Main example function"""
    print("🌟 ToneSoul System Basic Usage Example")
    print("=" * 50)
    
    # Initialize client
    client = ToneSoulClient()
    
    # 1. Health Check
    print("\n1. 🏥 Health Check")
    health = client.health_check()
    if health:
        print(f"✅ System is healthy: {health['status']}")
        print(f"   Version: {health['version']}")
        print(f"   Timestamp: {health['timestamp']}")
    else:
        print("❌ System is not responding. Make sure ToneSoul is running.")
        return
    
    # 2. Basic Processing
    print("\n2. 🧠 Basic Sentence Processing")
    test_sentences = [
        "Hello, how are you today?",
        "I promise to help you with this project",
        "Thank you for your assistance",
        "I'm feeling a bit confused about this topic"
    ]
    
    for sentence in test_sentences:
        print(f"\n   Input: '{sentence}'")
        result = client.process_sentence(sentence)
        
        if result:
            print(f"   ✅ Success: {result['success']}")
            print(f"   🎯 Intent: {result['intent_type']}")
            print(f"   🎭 Function: {result['tone_function']}")
            print(f"   ⏱️  Latency: {result['total_latency_ms']}ms")
            print(f"   💬 Response: {result['module_response'][:100]}...")
            
            # Show evolution insights if available
            if 'evolution_insights' in result:
                insights = result['evolution_insights']
                print(f"   🧠 Learning: {insights['adaptive_learning']['learning_opportunities_detected']} opportunities")
                print(f"   🤔 Cognitive: {insights['metacognitive_analysis']['cognitive_state']}")
                print(f"   📚 Knowledge: {insights['knowledge_evolution']['knowledge_extracted']} items extracted")
        else:
            print("   ❌ Processing failed")
    
    # 3. Evolution Status
    print("\n3. 🔄 Evolution Status")
    evolution = client.get_evolution_status()
    if evolution:
        print("   ✅ Evolution system active")
        if 'adaptive_learning' in evolution:
            learning = evolution['adaptive_learning']
            print(f"   📈 Most active patterns: {len(learning.get('most_active_patterns', []))}")
        
        if 'metacognitive' in evolution:
            cognitive = evolution['metacognitive']
            print(f"   🧠 Cognitive state: {cognitive.get('current_state', 'unknown')}")
            print(f"   🎯 Self-awareness: {cognitive.get('system_self_awareness_score', 0):.2f}")
        
        if 'knowledge_evolution' in evolution:
            knowledge = evolution['knowledge_evolution']
            print(f"   📚 Knowledge nodes: {knowledge.get('total_knowledge_nodes', 0)}")
            print(f"   💚 Knowledge health: {knowledge.get('knowledge_health_score', 0):.2f}")
    
    # 4. Manual Reflection
    print("\n4. 🤔 Manual Reflection")
    reflection = client.trigger_reflection()
    if reflection:
        print("   ✅ Reflection triggered successfully")
        if 'reflection_results' in reflection:
            results = reflection['reflection_results']
            print(f"   🧠 Cognitive state: {results.get('cognitive_state', 'unknown')}")
            print(f"   🎯 Decision confidence: {results.get('decision_confidence', 0):.2f}")
            print(f"   ⚖️  Biases detected: {len(results.get('biases_detected', []))}")
    
    print("\n" + "=" * 50)
    print("🎉 Example completed! ToneSoul is working properly.")
    print("\n💡 Try running this example multiple times to see how")
    print("   the system learns and evolves from each interaction!")


if __name__ == "__main__":
    main()