# Wordle AI

currently working on this along. 

> A hybrid Wordle-solving system combining deterministic constraint solving with language-model reasoning.

Wordle AI is an experimental AI project designed to explore how traditional algorithmic reasoning can be combined with small language models.

Instead of relying entirely on an LLM to solve Wordle, the system uses deterministic Wordle constraints to reduce the search space and investigates how a compact language model can assist with word selection and reasoning.

---

## Objectives

The project explores:

- Wordle game logic
- Constraint-based search
- Candidate word filtering
- Language-model reasoning
- LLM post-training
- Small-model experimentation
- Hybrid AI system design

---

## How Wordle Works

Each guess receives feedback using three states:

```text
🟩 Green  → Correct letter and correct position
🟨 Yellow → Correct letter but wrong position
⬜ Gray   → Letter is not present

                Wordle Game
                     |
                Initial Guess
                     |
              Generate Feedback
                     |
              Constraint Engine
                     |
          +----------+----------+
          |                     |
    Valid Candidates       Eliminated Words
          |
       Ranking
          |
     +----+----+
     |         |
 Algorithm    LLM
     |         |
     +----+----+
          |
       Next Guess
          |
        Result