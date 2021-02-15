#!/usr/bin/env python3
import argparse


def node_list(args):
    print("Execute node list command")
    print(args)


def pod_list(args):
    print("Execute pod list command")
    print(args)


def pod_delete(args):
    print("Execute pod delete command")
    print(args)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="resource", help="target resource")
    # Note: In advance `dest` key word arg. of add_subparsers() must be set.
    subparsers.required = True
    # Alternative: (Python 3.7 or later)
    # subparsers = parser.add_subparsers(
    #     dest="resource", required=True, help="target resource"
    # )

    parser_node = subparsers.add_parser("node", help="manage nodes")
    subparser_node = parser_node.add_subparsers(dest="verb", help="operation")
    subparser_node.required = True

    parser_node_list = subparser_node.add_parser("list", help="list nodes.")
    parser_node_list.set_defaults(cmd_func=node_list)

    parser_pod = subparsers.add_parser("pod", help="manage pods")
    subparser_pod = parser_pod.add_subparsers(dest="verb", help="operation")
    subparser_pod.required = True

    parser_pod_list = subparser_pod.add_parser("list", help="list pods")
    parser_pod_list.set_defaults(cmd_func=pod_list)

    parser_pod_delete = subparser_pod.add_parser("delete", help="delete a pod")
    parser_pod_delete.add_argument("name", help="pod name")
    parser_pod_delete.set_defaults(cmd_func=pod_delete)

    args = parser.parse_args()

    if hasattr(args, "cmd_func"):
        args.cmd_func(args)
    else:
        args.cmd_help()


if __name__ == "__main__":
    main()
