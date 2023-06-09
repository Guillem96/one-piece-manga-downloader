import asyncio
import shutil
import tempfile
from pathlib import Path
from typing import Iterator

import pytest


@pytest.fixture
def tempdir() -> Iterator[Path]:
    tmp_dir = tempfile.mkdtemp()
    yield Path(tmp_dir)
    shutil.rmtree(tmp_dir)


@pytest.fixture
def async_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.new_event_loop()
    yield loop
    loop.stop()
    loop.close()
