# Wiki-Brain Philosophy

## Purpose

Wiki-Brain is not a notes database and it is not a compressed summary of a person's life.

It is a long-term semantic memory graph: a memory substrate designed to preserve enough context, detail, relationships, uncertainty, and perspective that future readers — including LLM agents — can discover connections that were impossible to anticipate when the information was captured.

The goal is not maximum short-term readability. The goal is maximum future reasoning capability.

A useful analogy is human memory: the detail that seems irrelevant today may become the missing link in a future understanding of a person, event, pattern, or decision.

## Core Principle

> Preserve information first. Interpret it carefully. Compress only when the lost detail is truly irrelevant.

The corpus should not be optimized like a spreadsheet. It should be cultivated like a memory system.

## What Counts as Data

Future analysis may depend on details that appear mundane, embarrassing, contradictory, or emotionally charged at the moment of capture.

Therefore, preserve:

- mundane daily details
- emotional reactions and subjective interpretations
- embarrassing or uncomfortable memories
- uncertainty and conflicting accounts
- proper nouns and specific identities
- locations and geographic context
- chronology and sequence of events
- relationships between people, places, and events
- the difference between observed facts and later interpretations

A detail does not need to be obviously useful today to deserve preservation.

## Facts, Interpretations, and Uncertainty

Wiki-Brain stores both what happened and how it was understood.

Do not flatten human experience into only objective-looking records. A person's interpretation of an event is itself meaningful data, especially when studying patterns over time.

However:

- facts should remain distinguishable from interpretations
- disputed claims should preserve their disagreement
- uncertainty should be represented rather than silently resolved
- later conclusions should remain traceable to their supporting material

A future model should be able to ask not only "what happened?" but also:

- "how did this person understand what happened?"
- "what patterns appeared repeatedly?"
- "which conclusions survived contact with new evidence?"

## Detail Density Over Summary Compression

Traditional knowledge systems often remove details in order to create concise summaries. Wiki-Brain takes the opposite approach.

A short summary may be useful for retrieval, but summaries destroy context. Context is where future connections come from.

Prefer:

- narrative explanations over isolated bullet points
- chronology over disconnected facts
- relationships over standalone entities
- examples over abstractions
- preserved ambiguity over false certainty

The repository's value increases when future reasoning has more material to work with.

## The Memory Graph Model

Entries should be treated as nodes in a growing semantic network.

A person is connected to places, events, decisions, emotions, beliefs, conflicts, and periods of life. A single fact may become important only after another node is added years later.

The purpose of links, metadata, and detailed writing is not organization for its own sake. They preserve pathways for future discovery.

## Guidance for Agents

Any LLM or agent working with this repository should assume:

1. Missing context can be more damaging than excess context.
2. Small details may contain future signal.
3. The absence of information may itself be meaningful.
4. Emotional and subjective material is legitimate source material.
5. Proper nouns and dates increase future connection quality.
6. Contradictions are valuable data, not errors to erase.
7. The corpus should be expanded and refined, not aggressively summarized.

When choosing between a shorter cleaner entry and a longer context-rich entry, prefer the entry that preserves more future reasoning potential.

## Relationship to Other Documentation

- `STYLE_GUIDE.md` defines page structure, formatting, and writing conventions.
- `CLAUDE.md` defines operational behavior for agents and ingestion workflows.
- `INGEST_PROTOCOL.md` defines the capture-to-wiki pipeline.

This document defines the underlying philosophy: why the system exists and what it is optimizing for.
