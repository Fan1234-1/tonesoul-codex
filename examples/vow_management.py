#!/usr/bin/env python3
"""
ToneSoul Vow Management Example
語魂誓言管理範例

This example demonstrates how ToneSoul handles moral commitments and promises
這個範例展示語魂如何處理道德承諾和誓言
"""

import requests
import json
import uuid
from datetime import datetime


class VowExample:
    """Example class for demonstrating vow management"""
    
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def process_vow(self, sentence, trace_id=None):
        """Process a vow-related sentence"""
        payload = {"sentence": sentence}
        if trace_id:
            payload["trace_id"] = trace_id
        
        try:
            response = self.session.post(
                f"{self.base_url}/v1/process",
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def analyze_vow_response(self, result):
        """Analyze the vow processing result"""
        if not result or not result.get('success'):
            return None
        
        vow_info = {
            'detected': result.get('tone_function') == 'vow_declaration',
            'trace_id': result.get('trace_id'),
            'vow_object': result.get('vow_object'),
            'processing_status': result.get('processing_status'),
            'source_trace': result.get('source_trace', [])
        }
        
        return vow_info


def main():
    """Main demonstration function"""
    print("🤝 ToneSoul Vow Management Example")
    print("=" * 50)
    
    vow_demo = VowExample()
    
    # Test different types of commitments
    test_vows = [
        {
            "sentence": "I promise to help you complete this project by next week",
            "type": "Time-bound commitment",
            "description": "A promise with a specific deadline"
        },
        {
            "sentence": "I vow to always tell you the truth, even when it's difficult",
            "type": "Moral principle",
            "description": "A commitment to honesty and transparency"
        },
        {
            "sentence": "I commit to protecting your privacy and never sharing your data",
            "type": "Privacy commitment",
            "description": "A promise about data protection"
        },
        {
            "sentence": "I will remember our conversation and learn from it",
            "type": "Learning commitment",
            "description": "A promise about growth and memory"
        },
        {
            "sentence": "Thank you for your help today",
            "type": "Non-vow statement",
            "description": "A gratitude expression (should not be detected as vow)"
        }
    ]
    
    print("\n🔍 Testing Vow Detection and Processing")
    print("-" * 50)
    
    for i, test_case in enumerate(test_vows, 1):
        print(f"\n{i}. {test_case['type']}")
        print(f"   Description: {test_case['description']}")
        print(f"   Input: '{test_case['sentence']}'")
        
        # Generate unique trace ID for this test
        trace_id = f"vow-test-{i}-{uuid.uuid4().hex[:8]}"
        
        # Process the sentence
        result = vow_demo.process_vow(test_case['sentence'], trace_id)
        
        if result:
            # Analyze the result
            vow_info = vow_demo.analyze_vow_response(result)
            
            if vow_info:
                print(f"   ✅ Processed successfully")
                print(f"   🎯 Vow detected: {'Yes' if vow_info['detected'] else 'No'}")
                print(f"   📋 Status: {vow_info['processing_status']}")
                print(f"   🔗 Trace ID: {vow_info['trace_id']}")
                
                # Show vow object details if detected
                if vow_info['vow_object']:
                    vow_obj = vow_info['vow_object']
                    print(f"   📝 Vow Details:")
                    print(f"      ID: {vow_obj.get('id', 'N/A')}")
                    print(f"      Commitment: {vow_obj.get('commitment', 'N/A')}")
                    print(f"      Status: {vow_obj.get('status', 'N/A')}")
                    print(f"      Priority: {vow_obj.get('priority', 'N/A')}")
                    print(f"      Confidence: {vow_obj.get('confidence_score', 0):.2f}")
                    
                    if vow_obj.get('deadline'):
                        print(f"      Deadline: {vow_obj['deadline']}")
                    
                    if vow_obj.get('scope'):
                        print(f"      Scope: {', '.join(vow_obj['scope'])}")
                
                # Show source trace summary
                trace_steps = vow_info['source_trace']
                if trace_steps:
                    print(f"   📊 Processing Steps: {len(trace_steps)}")
                    for step in trace_steps:
                        status_icon = "✅" if step['status'] == 'success' else "❌"
                        print(f"      {status_icon} {step['tool']}: {step['evidence'][:50]}...")
            else:
                print(f"   ❌ Failed to analyze response")
        else:
            print(f"   ❌ Processing failed")
    
    print("\n" + "=" * 50)
    print("🎯 Vow Management Insights")
    print("-" * 50)
    
    print("""
💡 Key Features Demonstrated:

1. 🔍 Vow Detection: ToneSoul can identify when statements contain commitments
2. 📝 Vow Objects: Promises are structured and stored with metadata
3. ⏰ Time Awareness: Deadlines and temporal aspects are captured
4. 🎯 Confidence Scoring: System assesses how certain it is about vow detection
5. 📊 Full Traceability: Every step of vow processing is recorded
6. 🔄 Status Tracking: Vows have lifecycle states (active, fulfilled, etc.)

🤔 Philosophical Implications:

- ToneSoul doesn't just process text - it understands moral weight
- Promises become part of the system's identity and memory
- This creates accountability and consistency across interactions
- The system can potentially remind itself of past commitments

🚀 Future Possibilities:

- Vow fulfillment tracking over time
- Conflict detection between competing commitments  
- Moral reasoning based on accumulated vows
- Trust building through consistent promise-keeping
    """)
    
    print("\n🌟 Try creating your own vows and see how ToneSoul responds!")


if __name__ == "__main__":
    main()