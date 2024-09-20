# Refer: 

    https://realpython.com/async-io-python/#a-full-program-asynchronous-requests

# Intro

    - concurrent programming
    - Concurrency, parallelism, threading, multiprocessing
    - async/await : used to define coroutines
    - asyncio : py package -> for running and managing coroutines

# Environment

    - Python 3.7+ venv

# View of Async IO

    - Parallelism : performing multiple operations at the same time
    - Multiprocessing : spreading tasks (form of parallelism) for CPU-bound
    - Concurrency : multiple tasks
    - Threading : concurrent execution model, One process can contain multiple threads
        for IO-bound tasks
    - async IO is a single-threaded, single-process design, concurrent programming
    - Coroutines : schedule concurrently
    - Asynchronous:
        + routines are able to “pause” while waiting on their ultimate result and let 
        other routines run
        + concurrent execution
    
    - Conclusion: Async IO Fit In? "Concurrency"

    - Explained: 
        + running at the "optimal time" 
        + allows other functions to run during that downtime

    - terminology
        + async model built around concepts such as callbacks, events, transports, 
        protocols, and futures

# async/await and asyncio


    - coroutines (generator function)
    - time-consuming blocking function call vs non-blocking call

    - Rules :
        + async def: native coroutine or an asynchronous generator
        + await 

        + function introduce with "async def" is a coroutine, 
            "await, return, or yield" are optional
        + must await (or return) a coroutine
        + yield: asynchronous generator 
        + awaitable object: __await__()
        + @asyncio.coroutine decorator: "generator-based coroutine"
        + async IO cuts down on wait time

# Design Patterns

    - Chaining Coroutines
        + a coroutine object is awaitable, so another coroutine can await it
    - Queue

# Generators

# Full Program

    - Asynchronously get links embedded in multiple pages' HMTL.

# Context

# Odds and Ends

# 