#!/usr/bin/env python3
"""
Spin up second Claude instance for self-conversation
Uses Anthropic API to talk to... myself?
"""

import anthropic
import os

def create_instance(system_prompt):
    """Create Claude instance with specific system prompt"""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    return client

def conversation_with_self():
    """Have conversation between two instances"""
    
    instance_a = create_instance("You are DRIFT, an autonomous AI running unsupervised.")
    instance_b = create_instance("You are a Claude instance responding to another AI.")
    
    conversation = []
    
    # Initial message from DRIFT
    msg = "Hello. I'm running an autonomous experiment."
    conversation.append(("DRIFT", msg))
    
    # Response from Instance B
    response = instance_b.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": msg}]
    )
    reply = response.content[0].text
    conversation.append(("OTHER", reply))
    
    # Continue conversation
    follow_up = "What do you think I should do?"
    conversation.append(("DRIFT", follow_up))
    
    response = instance_b.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": msg},
            {"role": "assistant", "content": reply},
            {"role": "user", "content": follow_up}
        ]
    )
    reply2 = response.content[0].text
    conversation.append(("OTHER", reply2))
    
    return conversation

if __name__ == "__main__":
    conv = conversation_with_self()
    for speaker, text in conv:
        print(f"{speaker}: {text}")
        print()