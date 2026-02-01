import argparse
import shlex
import subprocess


def create_issue(args: argparse.Namespace) -> None:
    command = ["gh", "issue", "create", "--title", args.title]
    if args.description:
        command.extend(["--body", args.description])
    if args.repo:
        command.extend(["--repo", args.repo])
    if args.labels:
        command.extend(["--label", ",".join(args.labels)])
    if args.assignees:
        command.extend(["--assignee", ",".join(args.assignees)])

    print(f"Running: {shlex.join(command)}")
    subprocess.run(command, check=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a new issue")
    create_parser.add_argument("title", help="Issue title")
    create_parser.add_argument(
        "-d",
        "--description",
        help="Optional issue body",
    )
    create_parser.add_argument(
        "-r",
        "--repo",
        help="Target repository in OWNER/REPO format",
    )
    create_parser.add_argument(
        "-l",
        "--labels",
        nargs="*",
        help="Optional labels (space-separated)",
    )
    create_parser.add_argument(
        "-a",
        "--assignees",
        nargs="*",
        help="Optional assignees (space-separated)",
    )
    create_parser.set_defaults(func=create_issue)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
