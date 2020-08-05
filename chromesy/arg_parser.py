import argparse
import sys


def add_file_arg(parser):
    parser.add_argument(
        "-f",
        "--from",
        dest="from_file",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin
    )


def create_arg_parser():
    parser = argparse.ArgumentParser(
        prog="chromesy",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="mode")
    subparsers.required = True
    parser_export = subparsers.add_parser(
        "export",
        description="outputs a json file with the data"
    )
    parser_import = subparsers.add_parser(
        "import",
        description="imports a json file with the data to chrome",
    )
    add_file_arg(parser_import)
    add_file_arg(parser_export)
    return parser
