#!/bin/bash
# Run the crew agents with clean output (suppress stderr warnings)

uv run python app/agents/crew_agents.py 2>/dev/null
