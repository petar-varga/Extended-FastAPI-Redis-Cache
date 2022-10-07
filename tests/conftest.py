import os

import pytest

from extended_fastapi_redis_cache import FastApiRedisCache


@pytest.fixture(autouse=True)
def test_setup(request):
    """Setup TEST environment to use FakeRedis."""
    os.environ["CACHE_ENV"] = "TEST"
    redis_cache = FastApiRedisCache()
    redis_cache.init(host_url="")
    return True
