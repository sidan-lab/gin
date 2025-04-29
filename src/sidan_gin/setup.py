import os
import subprocess
import sys

from setuptools import Extension, find_packages, setup

# Try to get version from pyproject.toml
try:
    import tomli

    with open("pyproject.toml", "rb") as f:
        version = tomli.load(f)["tool"]["poetry"]["version"]
except (ImportError, FileNotFoundError):
    version = "0.1.3"  # Fallback version


# Build the Rust extension if not already built
def build_rust_extension():
    if not os.path.exists("src/sidan_gin/python_signing_module/src/libsigner.a"):
        subprocess.check_call(
            ["bash", "src/sidan_gin/python_signing_module/build.sh"],
            cwd="src/sidan_gin/python_signing_module",
        )


# Determine OS-specific configuration
platform_specific = {}
if sys.platform == "win32":
    platform_specific = {
        "extra_link_args": ["/DEFAULTLIB:advapi32.lib"],
    }
elif sys.platform == "darwin":  # macOS
    platform_specific = {
        "extra_link_args": [
            "-L/opt/homebrew/opt/openssl/lib",
            "-L/usr/local/opt/openssl/lib",
        ],
        "include_dirs": [
            "/opt/homebrew/opt/openssl/include",
            "/usr/local/opt/openssl/include",
        ],
    }
else:  # Linux
    platform_specific = {
        "libraries": ["ssl", "crypto"],
    }

# Try to build the extension
try:
    build_rust_extension()
except Exception as e:
    print(f"Warning: Could not build Rust extension: {e}")
    print("Will try to continue without it")

# Define the extension
cardano_signer_ext = Extension(
    "sidan_gin.python_signing_module.src._CardanoSigner",
    sources=[
        "src/sidan_gin/python_signing_module/src/signer_wrap.cxx",
        "src/sidan_gin/python_signing_module/src/signer.cpp",
    ],
    extra_objects=["src/sidan_gin/python_signing_module/src/libsigner.a"],
    include_dirs=["src/sidan_gin/python_signing_module/src/"],
    **platform_specific,
)

setup(
    name="sidan-gin",
    version=version,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    ext_modules=[cardano_signer_ext],
    python_requires=">3.11,<4.0.0",
    install_requires=[
        "requests>=2.25",
        "cbor2>=5.6.5",
        "pycardano>=0.12.3",
        "cryptography>=44.0.2",
    ],
    include_package_data=True,
)
