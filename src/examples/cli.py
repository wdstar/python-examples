#!/usr/bin/env python3
import argparse
import coloredlogs
import logging
import time
import sys

logger = logging.getLogger(__name__)


def log_sample(args):
    logger.debug("debug message.")
    logger.info("info message.")
    logger.warning("warning message.")
    logger.error("error message.")


def node_list(args):
    logger.info("Execute node list command")
    logger.info(args)


def pod_list(args):
    logger.info("Execute pod list command")
    logger.info(args)


def pod_delete(args):
    logger.info("Execute pod delete command")
    logger.info(args)


def main():
    logging.raiseExceptions = False
    logging.Formatter.converter = time.localtime
    # logging.Formatter.converter = time.gmtime
    """
    logging.basicConfig(
        # filename="sample.log",
        handlers=[logging.StreamHandler()],
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %Z %z",
    )
    """
    coloredlogs.install(
        stream=sys.stdout,  # default: sys.stderr
        level="DEBUG",
        fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %Z %z",
    )

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="resource", help="target resource")
    # Note: In advance `dest` key word arg. of add_subparsers() must be set.
    subparsers.required = True
    # Alternative: (Python 3.7 or later)
    # subparsers = parser.add_subparsers(
    #     dest="resource", required=True, help="target resource"
    # )

    parser_log = subparsers.add_parser("log", help="manage logs")
    subparser_log = parser_log.add_subparsers(dest="verb", help="operation")
    subparser_log.required = True

    parser_log_sample = subparser_log.add_parser("sample", help="sample logs.")
    parser_log_sample.set_defaults(cmd_func=log_sample)

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
