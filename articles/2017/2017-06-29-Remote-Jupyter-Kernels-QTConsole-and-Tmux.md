---
layout: post
title: Remote Jupyter Kernels, QTConsole, and Tmux
tags: tmux vim jupyter python aws wwe
---

This is a companion note to [Jupyter Notebook + Console](2017-06-29-jupyter-notebook-console.md)
and [TMux + Vim + AWS](2017-06-21-Tmux-Vim-AWS.md). The useful idea from the
old scratchpad was this:

> Jupyter is a kernel plus one or more user interfaces.

Once that clicks, a notebook does not have to be the only way into a running
Python session. A console, QTConsole, notebook, and editor-driven workflow can
all attach to the same kernel when the connection file is available.

## Local Sanity Check

Start a console and ask it for its connection info:

```bash
jupyter console
```

Inside that console:

```python
%connect_info
a = 2
```

Then, from another local terminal, connect another interface to the same kernel:

```bash
jupyter qtconsole --existing
```

If the second interface can evaluate `a`, it is attached to the same live
kernel. Exiting the original kernel owner will kill the shared session, so this
is mostly a way to understand the mechanism before using it remotely.

## Finding the Kernel File

The practical discovery was that Jupyter exposes the runtime directory directly:

```bash
jupyter --runtime-dir
```

The connection file is typically named like:

```text
kernel-<pid>.json
```

That file contains the ports, IP address, key, transport, signature scheme, and
kernel name needed by another Jupyter interface.

## Remote Kernel Recipe

The rough 2017 AWS workflow was:

```bash
# Local terminal
ssh username@remote-server

# Remote shell
jupyter --runtime-dir
ipython kernel &

# Local terminal
scp username@remote-server:/run/user/1001/jupyter/kernel-<pid>.json "$(jupyter --runtime-dir)"
jupyter qtconsole --existing --ssh=username@remote-server
```

The exact remote runtime directory can vary, which is why checking
`jupyter --runtime-dir` on the remote machine matters.

## Tmux-Oriented Workflow

For day-to-day work, the cleaner solution was not necessarily QTConsole. It was
to keep the remote machine organized with tmux and attach whichever Jupyter UI
made sense:

```text
1. Local: ssh username@remote-server
2. Remote: start tmux
3. Remote: start Jupyter Notebook without a browser
4. Local browser: open the forwarded notebook URL
5. Remote tmux pane: jupyter console --existing
6. Remote tmux pane: edit scripts in Vim
```

That gives a useful split:

- Vim for editing scripts, functions, and modules.
- Jupyter console for interactive execution.
- Notebook UI for plots, documentation, and longer exploratory records.

## Historical Note

This was a 2017 workflow. Today, VS Code Remote, JupyterLab, SSH forwarding, and
managed notebooks make much of this smoother. Still, the underlying lesson holds
up: once the kernel/UI split is clear, Jupyter becomes a more flexible tool than
"open a notebook and type in cells."
