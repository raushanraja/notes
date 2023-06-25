### Asyncio
- asyncio allows to write **concurrent** code using **async/await** syntax.
- Offer perfect to write IO-bound and high level network structured code.
- asyncio library provides high level api to:
  - Runners
  - Run coroutines concurrently. 
  - Perform network IO and IPC.
  - Control subprocesses.
  - Distribute tasks via queues.
  - Synchronize concurrent code.
- Low level api:
  - Create and manage event loops.
  - Running subprocesses.
  - Handling OS signals.
  - Implement efficient protocols using transports.
  - Bridge callback-based libraries and code with async/await syntax.



#### Runners:
  - These are main entry points for asyncio programs.
  - There are built on top of event loop to simplify async/await programming.
  - Running a coroutine:
    - Syntax: `asyncio.run(coro, * , debug=None)`:
    ```python
          async def main():
              await asyncio.sleep(1)
              print('hello')

          asyncio.run(main())
      ```

  - Runner Context Manager
    - A context manager 
    - It simplifies multiple async function call in the same context.
    - Sometimes several top-level async functions can be called in same event loop and contextvars.Context.

    - syntax: `asyncio.Runner(*, debug=None, loop_factory=None)`
    ```python
          async def main():
            await asyncio.sleep(1)
            print('hello')

          with asyncio.Runner() as runner:
            runner.run(main())
      ```


#### Coroutines:
- A coroutine is a function 
  - That can be entered exited and resumed at many different points.
- It is the preferred way of writing asyncio application.
- Implemented with `async def` statement.
- Methods to run a coroutine:
  - Using the **Runner** : `aysncio.run()`
  - Using the **Runner Context Manager**: `asyncio.Runner()`
  - Using **Create Task**: `asyncio.create_task()`
  - Using **TaskGroup Context Manager**: `asyncio.TaskGroup()`

  ```python
      async def main():
        print('hello, waiting for 3 seconds')
        await asyncio.sleep(3)
        print('world')


      async def say_what(delay,what):
        await asyncio.await(delay)
        print(what)

      # Using Runner: asyncio.run()
      asyncio.run(main())

      # Using Runner Context Manager: 
      with asyncio.Runner() as runner:
        runner.run(main())

      # Using Create Task
      task1 = asyncio.create_task(say_what(1,'hello'))
      task2 = asyncio.create_task(say_what(2,'world'))

      async def run_tasks():
        await task1
        await task2

      aysncio.run(run_tasks())

      # Using TaskGroup Context Manager
      async def run_tasks():
        async with asyncio.TaskGroup() as tg:
          print('Before running tasks')
          task1 = tg.create_task(say_what(1,'hello'))
          task2 = tg.create_task(say_what(2,'world'))
          print('After running tasks')
          # await is implicit in context Manager

      asyncio.run(run_tasks())
  ```
