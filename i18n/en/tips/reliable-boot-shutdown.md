# Reliably doing something when a ghost starts and shuts down

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

This describes how to reliably do something when a ghost loads or shuts down, such as loading a resident SAORI or initializing variables.

### To start with...

The method is simple. In an appropriate dictionary, write:

```
OnGhostLoad
{
  起動時のごにょごにょ
}

OnGhostUnload
{
  終了時のごにょごにょ
}
```

That is all.

Note that **nothing will happen if you write a script here.**<br>
This is only for basic initialization. Be sure to write dialogue in OnBoot and other appropriate events.

### To make it even more reliable

SSP has a feature called the ghost cache mechanism, which keeps a ghost that has been loaded once in memory in preparation for reloading it.<br>
If you absolutely need to do something reliably when a ghost is opened or closed, in addition to the above,

```
OnCacheSuspend
OnCacheRestore
```

you need to write something in these.

...Well, normally you probably don't need to worry about it much.
