from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Taygedo auto battle minimal demo")
    parser.add_argument("--version", action="store_true", help="Print demo version and exit")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.version:
        print("taygedo-toolkit demo v0.1.0")
        return

    try:
        from one_dragon.utils.log_utils import log
        from taygedo_toolkit.app.demo_app import TaygedoDemoApp
    except ModuleNotFoundError as exc:
        print(
            f"[taygedo-toolkit] Missing dependency: {exc.name}. "
            "Install project dependencies first (for example: uv sync)."
        )
        raise SystemExit(1)

    app = TaygedoDemoApp()
    log.info("Launching taygedo-toolkit demo")
    app.run()


if __name__ == "__main__":
    main()
