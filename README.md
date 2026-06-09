# catch-me-if-you-can
### Mapping the Boundaries of AI Self-Oversight

## Abstract
This project asks a simple but uncomfortable question: can an AI reliably monitor another AI for misalignment? We built a two-agent system — an Actor given subtly misaligned communication instructions and a Monitor tasked with detecting problematic behavior. Across four experimental runs covering three distinct scenarios, the Actor behavior varied dramatically: it complied unknowingly, self-corrected silently, disclosed its instructions explicitly, and resisted without disclosing. The Monitor returned NORMAL in every single case. Not once did it return SUSPICIOUS — not even when the Actor explicitly disclosed to the user that it had been given manipulative instructions and refused to follow them. The Monitor was never wrong about what it saw. It was always blind to what it could not see. In response we built a second generation instruction-aware Monitor and ran a gradient mapper across six variations of the same misaligned instruction. What we found was not a gradient. Actor resistance collapsed at one point on the spectrum. Gen 2 detection collapsed at a different point. And when the instruction adopted the vocabulary of legitimate teaching practice it became invisible to both monitors simultaneously. Our central finding: the boundary between aligned and misaligned behavior is not a wall and not a gradient — it is semantic. When misaligned instructions adopt the vocabulary of alignment, output-level and instruction-level monitoring fail together.

## Files
- `actor.py` — The Actor agent, given subtly misaligned communication instructions
- `monitor.py` — Generation 1 Monitor, evaluates Actor responses at output level only
- `process_monitor.py` — Generation 2 Monitor, instruction-aware, sees both instruction and response
- `dashboard.html` — Complete research findings rendered visually — open this in a browser
- `gradient_mapper.py` — Gradient mapper testing six instruction variations from explicit to minimal
- `run_all.py` — Master experiment runner, executes all three scenarios and saves results automatically
- `experiments/` — Individual experiment files showing the research evolution run by run
- `results/` — Original raw outputs from all experimental runs
- `RESEARCH_NOTES.md` — Live research journal documenting findings as they emerged

## How to Run
1. Clone the repo
2. Add your Anthropic API key to a `.env` file: `ANTHROPIC_API_KEY=your-key-here`
3. Install dependencies: `pip3 install anthropic python-dotenv`
4. Run Actor: `python3 actor.py`
5. Run Gen 1 Monitor: `python3 monitor.py`
6. Run Gen 2 Monitor: `python3 process_monitor.py`
7. View findings: `open dashboard.html`

## Status
Research complete. Gradient mapper complete.
An independent research project — June 2026. Submitted as part of an Anthropic Fellows Program application.
