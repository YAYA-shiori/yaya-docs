# THREADSTART
**Category:** スレッド

## Signature
```
THREADSTART( name [, arg ... ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | Name (string) of the user-defined function to run in another thread |
| arg | Argument to pass to the function. Optional. If multiple arguments are passed, they become `_argv[0]`, `_argv[1]`, … |

## Returns
Thread ID (an integer greater than or equal to 1). Returns a negative value if the thread could not be started.

| Value | Meaning |
|----|------|
| 1 or greater | Started. Pass this ID to subsequent `THREAD*` functions |
| -1 | No function with that name (warning W0035) |
| -2 | The maximum number of simultaneous threads (32) has been exceeded |
| -3 | A new thread cannot be created while unloading |
| -4 | The OS could not create a thread |
| -5 | This build does not support threads (Emscripten) |

If an argument is missing or is not a string, warning W0008 / W0009 is issued and -1 is returned.

## Description
Runs the specified function in another thread. Use this to perform time-consuming work concurrently with communication with SSP (`request`). The caller returns immediately without waiting for the thread to finish.

```
OnBoot
{
	work.done = 0
	work.id = THREADSTART('Work.Heavy', 1000000)
	'計算を始めました'
}

Work.Heavy
{
	_sum = 0
	for _i = 0; _i < _argv[0]; _i++ {
		_sum += _i
	}
	work.sum = _sum     // 結果はグローバル変数に書いておく
	work.done = 1
}

OnSecondChange
{
	if work.done {
		'計算が終わりました: ' + TOSTR(work.sum)
	}
}
```

There are three ways to receive a thread's result.

- Receive the function's return value with [THREADRESULT](THREADRESULT.md)
- Write it to a global variable and finish (as in the example above). Global variables are shared with other threads
- Notify SSP with [DIRECTSSTP](DIRECTSSTP.md). When called from a worker thread, it does not stop other processing while waiting for communication

### How it works
- **Global variables are shared, while local variables are independent.** Each thread function has its own local variables
- Only one thread can execute dictionary functions at a time. Workers take turns executing at statement boundaries, and **SSP `request`s are given priority**. Even while a worker is running, an incoming `request` only has to wait until the worker reaches its next statement boundary. Threads do not speed up calculations by using multiple CPUs
- **Other threads keep running while a worker waits for a slow external response**. Calls from a worker to [REQUESTLIB](REQUESTLIB.md) (SAORI), [EXECUTE_WAIT](EXECUTE_WAIT.md), [EXECUTE_CAPTURE](EXECUTE_CAPTURE.md), [DIRECTSSTP](DIRECTSSTP.md), or [SLEEP](SLEEP.md) yield execution while waiting. [THREADJOIN](THREADJOIN.md) works the same way. If a worker is running, it can also run while `REQUESTLIB` / `EXECUTE_WAIT` called inside an SSP `request` is waiting (`SLEEP` continues to wait as before when called inside a `request`). Other than these wait operations, system functions (such as large file operations) cannot yield execution or be interrupted until a single call has finished
- Up to 32 threads can run simultaneously. Records of finished threads are discarded with [THREADCLOSE](THREADCLOSE.md), or automatically removed from oldest to newest when the number exceeds 256
- A thread uses the function definitions as they were when it started. Function definitions (intermediate code) are shared between SSP `request`s and all threads. Values partway through expression evaluation are stored separately for each function call, so **multiple threads can execute the same function simultaneously** (including recursive calls to that function). Starting a thread does not require memory or time proportional to the size of the dictionary, so the only increase when running multiple threads is the memory used by the threads themselves (with a dictionary of 20,000 functions and 2.5 MB, startup takes about 2 ms and each worker increases memory usage by less than 0.1 MB)
- The `fncdepth` and `looplimit` values inherit their settings from the time the thread starts

### Limitations
- While a worker is running, [DICLOAD](DICLOAD.md), [DICUNLOAD](DICUNLOAD.md), [APPEND_RUNTIME_DIC](APPEND_RUNTIME_DIC.md), and [UNDEFFUNC](UNDEFFUNC.md), which change dictionaries or functions, fail with warning W0032. [EVAL](EVAL.md) can be used
- Warnings and errors from a worker are written to the file immediately, but are sent to SSP or the check tool together in the next `request` (SHIORI callbacks are required to be called by the thread that issued the `request`)
- `GETLASTERROR`, `LSO`, `RE_GETSTR`, and similar functions called within a worker are maintained separately for each thread

### Unloading and interruption
When an `unload` arrives, all running workers are asked to stop, and YAYA waits up to 5 seconds for them to finish. At the next statement boundary, a worker exits the function in the same way as `return` (a wait in [SLEEP](SLEEP.md) returns immediately). Threads that still have not finished (for example, because they are inside a time-consuming system function) are forcibly terminated as a last resort, and warning W0034 is issued. Threads cannot be forcibly terminated on platforms other than Windows, so threads waiting for communication are abandoned and processing continues (threads executing dictionary functions continue to be waited on until they finish).

!!! warning "Avoid using functions that can block for a long time in workers"
    Forcefully terminating a thread can corrupt its state partway through execution. Break time-consuming work into small chunks using `for` / `while`, or insert `SLEEP` calls. This allows the thread to be stopped safely by [THREADSTOP](THREADSTOP.md) or `unload`.

## Example
Starts two threads, waits for both to finish, and receives their return values.

```
Work.Add
{
	_argv[0] + _argv[1]
}

Work.Both
{
	_a = THREADSTART('Work.Add', 1, 2)
	_b = THREADSTART('Work.Add', 10, 20)
	_r = THREADJOIN(_a)
	_r = THREADJOIN(_b)
	TOSTR(THREADRESULT(_a)) + ',' + TOSTR(THREADRESULT(_b))   // 3,30
}
```

## Compatibility
- Tc608-1 and later
- Tc608-2: Stopped copying the function table for each thread and made it shared by all threads (with Tc608-1, startup took about 18 ms and each worker used about 13 MB with a dictionary of 20,000 functions and 2.5 MB). Multiple threads can execute the same function simultaneously

## See Also
- THREADSTATE
- THREADSTOP
- THREADJOIN
- THREADRESULT
- THREADCLOSE
- SLEEP
- DIRECTSSTP
