import pytest
import subprocess
from deployer.env.go import GoEnvironment as Env


@pytest.fixture(scope="module")
def bootstrap():
    # make settable by env var
    current_env = subprocess.check_output("juju env", shell=True).strip()
    # make switchable by env var
    subprocess.check_call('juju bootstrap --upload-tools')
    return current_env


@pytest.yield_fixture(scope="module")
def juju_environment(bootstrap):

    current_env = subprocess.check_output("juju env", shell=True).strip()
    env = Env(current_env, None)
    yield Env
    env.reset(terminate_machines=True)
