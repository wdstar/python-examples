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
    parser.set_defaults(cmd_help=parser.print_help)
    subparsers = parser.add_subparsers(help="sub-command")

    parser_node = subparsers.add_parser("node", help="manage nodes")
    parser_node.set_defaults(cmd_help=parser_node.print_help)
    subparser_node = parser_node.add_subparsers()

    parser_node_list = subparser_node.add_parser("list", help="list nodes.")
    parser_node_list.set_defaults(cmd_func=node_list)

    parser_pod = subparsers.add_parser("pod", help="manage pods")
    parser_pod.set_defaults(cmd_help=parser_pod.print_help)
    subparser_pod = parser_pod.add_subparsers()

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
