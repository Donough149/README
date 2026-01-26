# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Repository Overview

**Name:** README
**Owner:** Donough149
**Status:** New/Minimal repository

This is a starter repository that currently contains placeholder README files. It serves as a foundation for future development.

## Current Structure

```
/
├── README          # Empty placeholder file
├── README.md       # Project title placeholder
└── CLAUDE.md       # AI assistant guidance (this file)
```

## Development Guidelines

### Git Workflow

1. **Branch Naming:** Use descriptive branch names following the pattern `feature/description`, `fix/description`, or `docs/description`
2. **Commits:** Write clear, concise commit messages in imperative mood (e.g., "Add feature X" not "Added feature X")
3. **Pull Requests:** Create PRs with descriptive titles and summaries

### Code Standards

When code is added to this repository:

- Follow language-specific best practices and conventions
- Include appropriate documentation and comments
- Write tests for new functionality
- Keep files organized in logical directory structures

### File Organization Conventions

As the repository grows, organize files as follows:

- `/src` - Source code
- `/tests` - Test files
- `/docs` - Documentation
- `/scripts` - Utility scripts

## For AI Assistants

### Before Making Changes

1. Read relevant existing files to understand context
2. Check git status and current branch
3. Understand the scope of requested changes

### When Implementing Features

1. Make minimal, focused changes
2. Avoid over-engineering or adding unrequested features
3. Follow existing patterns and conventions in the codebase
4. Test changes when possible

### Commit Guidelines

- Create atomic commits (one logical change per commit)
- Never commit sensitive information (API keys, credentials, etc.)
- Verify changes compile/run before committing

### Communication

- Explain changes clearly and concisely
- Note any assumptions made
- Flag potential issues or concerns

## Quick Reference

| Task | Command |
|------|---------|
| Check status | `git status` |
| View history | `git log --oneline` |
| Create branch | `git checkout -b branch-name` |
| Push changes | `git push -u origin branch-name` |
