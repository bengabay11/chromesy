import argparse
import getpass
import sys


def create_import_parser(subparsers):
    parser_import = subparsers.add_parser(
        "import",
        description="imports a json file with the data to chrome",
    )
    parser_import.add_argument(
        "-f",
        "--from",
        dest="from_file",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin
    )


def create_export_parser(subparsers):
    parser_export = subparsers.add_parser(
        "export",
        description="outputs a json file with the data"
    )
    parser_export.add_argument(
        "-d",
        "--destination",
        dest="destination_folder",
        type=str,
        help="destination folder to export the files",
        default=getpass.getuser()
    )


def create_arg_parser():
    parser = argparse.ArgumentParser(
        prog="chromesy",
        description="Import and Export chrome data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="mode")
    subparsers.required = True
    create_import_parser(subparsers)
    create_export_parser(subparsers)
    parser.add_argument(
        "-u",
        "--user",
        dest="user",
        type=str,
        default=getpass.getuser()
    )
    return parser
