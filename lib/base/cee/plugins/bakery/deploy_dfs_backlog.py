#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from pathlib import Path
from typing import Any, Dict

from cmk.base.api.bakery.function_types import (
    FileGenerator,
    Plugin,
    BakeryPlugin,
)
from cmk.base.api.bakery.constants import OS


def get_dfs_backlog_plugin(conf: Dict[str, Any]) -> FileGenerator:
    """generate agent bakery plugins"""
    if not conf.get("deploy"):
        return

    yield Plugin(base_os=OS.WINDOWS, source=Path("dfs_backlog.ps1"))

dfs_backlog_plugin = BakeryPlugin(
    name="dfs_backlog",
    files_function=get_dfs_backlog_plugin,
)