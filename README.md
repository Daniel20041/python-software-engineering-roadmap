# Python Software Engineering Roadmap

A structured software engineering learning journey focused on progressing from Python fundamentals to building production-style backend applications and becoming capable of solving technical interview and real-world engineering problems independently.

This repository documents my progress through approximately **120 progressively harder exercises**, projects, coding challenges, and engineering checkpoints.

The goal is not simply to learn Python syntax.

The goal is to develop the ability to:

- break down unfamiliar problems
- design solutions independently
- write clean and maintainable code
- debug software
- use Git confidently
- write automated tests
- work with APIs and databases
- build backend applications
- understand algorithms and data structures
- read technical documentation
- work with unfamiliar code
- complete technical interview and take-home tasks independently

---

# Current Progress

**Current stage:** Python Fundamentals

**Current exercise:** Exercise 7

Topics covered so far include:

- variables
- user input
- type conversion
- arithmetic
- f-strings
- conditional logic
- Boolean values
- `if / elif / else`
- `and / or`
- input validation
- basic test-case thinking
- Git staging
- Git commits
- GitHub pushes
- inspecting changes with Git

---

# Learning Method

Before writing code, problems are broken down using:

### INPUT
What information does the program receive?

### OUTPUT
What should the program produce?

### RULES
What conditions and requirements must be followed?

### DATA
What information needs to be stored?

### STEPS
How would the problem be solved manually?

### EDGE CASES
What unusual or boundary situations could occur?

The amount of guidance will gradually decrease throughout the roadmap.

Early exercises provide clearer specifications.

Later exercises will increasingly resemble real software-engineering work where I am expected to:

1. interpret requirements
2. design the solution
3. implement it
4. test it
5. debug it
6. refactor it
7. explain my decisions

---

# Roadmap

## Stage 1 — Core Python
**Exercises 1–20**

Topics:

- variables
- data types
- arithmetic
- input/output
- conditions
- Boolean logic
- loops
- strings
- lists
- dictionaries
- functions
- basic problem solving
- Git fundamentals

The focus during this stage is developing strong programming fundamentals rather than rushing into frameworks.

---

## Stage 2 — Problem Solving
**Exercises 20–35**

Topics:

- more advanced functions
- files
- exceptions
- modules
- object-oriented programming
- debugging
- program organisation
- deeper problem solving

LeetCode practice will begin during this stage.

---

## Stage 3 — APIs and External Data
**Exercises 35–50**

Topics:

- HTTP
- REST APIs
- JSON
- API requests
- authentication
- environment variables
- external services
- error handling

Projects will begin interacting with real external APIs.

---

## Stage 4 — Backend Development
**Exercises 50–70**

Topics:

- FastAPI / Flask
- SQL
- relational databases
- CRUD operations
- REST API design
- backend architecture
- automated testing
- API testing

At this stage the exercises will begin resembling junior backend engineering work.

---

## Stage 5 — Software Engineering
**Exercises 70–90**

Topics:

- larger backend applications
- project architecture
- authentication
- testing strategies
- Git branches
- Docker
- deployment
- CI/CD
- refactoring
- maintainability

The focus will shift from writing individual programs to building complete software systems.

---

## Stage 6 — Technical Interview Preparation
**Exercises 90–110**

Topics:

- algorithms
- data structures
- debugging unfamiliar code
- refactoring
- code review
- timed coding challenges
- system thinking
- technical interview questions

---

## Stage 7 — Advanced Engineering Challenges
**Exercises 110–120**

Topics:

- ambiguous engineering requirements
- larger technical tasks
- take-home assignments
- Quantcast-style coding challenges
- mock technical interviews
- code review
- GitHub portfolio improvement
- CV/project preparation

The goal at this stage is to be able to receive a technical specification and independently design, build, test and explain the solution.

---

# Extra Learning Checkpoints

The numbered exercises are only part of the roadmap.

Additional independent work is included throughout the journey.

## Around Exercises 15–20

- Build a small program without being given a specification
- Use Git entirely from the terminal
- Write my own project README

---

## Around Exercise 30

Build a small CLI application from scratch.

Requirements will include:

- multiple Python files
- input validation
- error handling
- basic automated tests

---

## Around Exercise 45

Work with a real external API.

Skills:

- make API requests
- read JSON
- extract useful data
- handle API errors
- use environment variables for API keys

---

## Around Exercise 60

Build my own REST API.

The project will include:

- API endpoints
- database integration
- CRUD operations
- endpoint testing

---

## Around Exercises 75–80

Build a complete backend project containing:

- REST API
- database
- authentication
- automated tests
- Git branches
- Docker
- deployment

---

## Around Exercise 90+

Begin more realistic interview preparation:

- timed coding exercises
- debugging unfamiliar code
- code review
- refactoring
- technical interview questions
- take-home assignments
- Quantcast-style engineering tasks

---

# LeetCode Plan

LeetCode is being introduced gradually rather than replacing software development practice.

## Around Exercise 20

**2–3 problems per week**

Topics:

- arrays
- strings
- loops
- conditionals
- dictionaries / hash maps

---

## Around Exercises 40–50

Approximately **one problem most study days**.

Mix of:

- Easy problems
- easier Medium problems
- SQL problems

---

## Around Exercise 70+

Approximately **3–5 deliberate problems per week**.

For each problem I should be able to explain:

- my approach
- why it works
- time complexity
- space complexity
- edge cases
- alternative solutions

---

# Projects

As the roadmap progresses, the repository will move away from isolated exercises and toward complete applications.

Potential projects include:

- Trading Journal API
- Trading Analytics Platform
- Personal Finance / Budget API
- Job Application Tracker
- Automated Schedule Planner
- REST API with authentication
- Database-backed backend applications

Projects will increasingly include:

- multiple modules
- databases
- authentication
- automated tests
- APIs
- documentation
- Docker
- deployment

---

# Git Workflow

Git is being used throughout the roadmap instead of being learned separately at the end.

Typical workflow:

```bash
git status
git diff
git add <file>
git diff --staged
git commit -m "commit message"
git push
git status
```

As projects become more complex, this will expand to include:

- branches
- merges
- pull requests
- resolving conflicts
- reverting changes
- collaborative Git workflows

---

# Repository Structure

The repository will gradually follow a structure similar to:

```text
python-software-engineering-roadmap/
│
├── week-01-python-fundamentals/
│   ├── day-01/
│   │   ├── exercise_01/
│   │   ├── exercise_02/
│   │   └── ...
│   │
│   ├── day-02/
│   │   └── ...
│   │
│   └── ...
│
├── projects/
│   └── ...
│
├── README.md
└── .gitignore
```

The structure will evolve as exercises become larger applications.

---

# Progress Philosophy

The objective of this repository is **not to complete 120 exercises as quickly as possible**.

Progress means becoming increasingly capable of solving problems without assistance.

The expected progression is:

```text
Learn a concept
      ↓
Solve guided exercises
      ↓
Solve requirements independently
      ↓
Build small projects
      ↓
Debug unfamiliar problems
      ↓
Design larger systems
      ↓
Complete interview-style tasks
      ↓
Build software independently
```

A difficult exercise that requires debugging and reasoning is more valuable than several exercises completed without understanding.

---

# Long-Term Goal

By the end of this roadmap I want to be capable of independently:

- receiving an unfamiliar software requirement
- breaking it into smaller problems
- designing an appropriate solution
- writing maintainable code
- using Git professionally
- writing automated tests
- working with APIs
- working with SQL databases
- building backend services
- debugging unfamiliar problems
- reading documentation
- reasoning about algorithms
- explaining technical decisions
- completing technical interviews
- completing software-engineering take-home tasks

The final goal is **independent software engineering ability**, not simply knowing Python syntax.