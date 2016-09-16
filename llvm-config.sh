#!/usr/bin/env bash

# if the LLVM_CONFIG environment variable is not set, attempt to search for various
# known naming conventions of llvm-config, looking for the latest version

[[ -z ${LLVM_CONFIG} ]] \
    && LLVM_CONFIG=$(which llvm-config 2>/dev/null) \
    || LLVM_CONFIG=$(which llvm-config-3.9 2>/dev/null) \
    || LLVM_CONFIG=$(which llvm-config-3.8 2>/dev/null) \
    || LLVM_CONFIG=$(which llvm-config-mp-3.9 2>/dev/null) \
    || LLVM_CONFIG=$(which llvm-config-mp-3.8 2>/dev/null)

# On Windows, we need to convert the MSYS path to the absolute path of Windows,
# because llvm-config is run from cmd.exe.
if [[ ${OSTYPE} == msys ]]; then
  LLVM_CONFIG=$(cygpath -am ${LLVM_CONFIG})
fi

echo -n ${LLVM_CONFIG}
