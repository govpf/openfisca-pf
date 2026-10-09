#!/usr/bin/env bash
# Patch openfisca_core to use 64-bit numbers instead of 32-bit ones (see README, section 1.5).
# Targets the openfisca_core installed in the project's virtualenv (.venv by default).
# Usage: ./patch_openfisca_core.sh [path/to/venv]

set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
venv_dir="${1:-$project_dir/.venv}"
python="$venv_dir/bin/python"

if [ ! -x "$python" ]; then
    echo "No python found in virtualenv: $venv_dir" >&2
    exit 1
fi

core_dir="$("$python" -c 'import os, openfisca_core; print(os.path.dirname(openfisca_core.__file__))')" || {
    echo "openfisca_core is not installed in $venv_dir" >&2
    exit 1
}
echo "Patching $core_dir"

sed -i 's/numpy\.int32/numpy.int64/; s/numpy\.float32/numpy.float64/' "$core_dir/variables/config.py"
sed -i 's/numpy\.float32/numpy.float64/' "$core_dir/tools/__init__.py"

if grep -n 'numpy\.\(int\|float\)32' "$core_dir/variables/config.py" "$core_dir/tools/__init__.py"; then
    echo "Patch incomplete: 32-bit types remain (see lines above)" >&2
    exit 1
fi
echo "Done: openfisca_core now uses numpy.int64 and numpy.float64"
