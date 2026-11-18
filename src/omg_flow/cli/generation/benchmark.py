from __future__ import annotations

import os
import sys
from collections.abc import Sequence

_BENCHMARKS = {"text", "audio", "humanref", "artifact"}


def main(argv: Sequence[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    benchmark = "text"
    if args and args[0] in _BENCHMARKS:
        benchmark = args.pop(0)

    if benchmark == "text":
        from omg_flow.benchmarks.runners.text import main as run
    elif benchmark == "audio":
        from omg_flow.benchmarks.runners.audio import main as run
    elif benchmark == "humanref":
        from omg_flow.benchmarks.runners.humanref import main as run
    elif benchmark == "artifact":
        from omg_flow.benchmarks.runners.artifact import main as run
    else:
        raise AssertionError(f"unhandled benchmark: {benchmark}")

    run(args)


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    main()
