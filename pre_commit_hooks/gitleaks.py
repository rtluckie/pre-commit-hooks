import argparse
import re
from typing import AbstractSet
from typing import Optional
from typing import Sequence

from pre_commit_hooks.util import cmd_output


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--report', help='where to store report', )
    parser.add_argument('-c', '--config', help='location of config', )
    args = parser.parse_args(argv)

    report = args.report or None
    config = args.config or None
    cmd = "gitleaks --quiet --format=json --path=."
    if report:
        cmd += " --report={}".format(report)
    if config:
        cmd += " --config-path={}".format(config)
    try:
        cmd_output(*cmd.split())
    except CalledProcessError as excp:
        print(excp)
        return 1
    return


if __name__ == '__main__':
    exit(main())
