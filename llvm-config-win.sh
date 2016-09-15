#!/usr/bin/env bash

# $1: argument passed to llvm-config, such as --includedir.
#
# In binding.gyp, a backslash in CLANG_SEARCH_PATH causes an escape sequence,
# which leads to build errors in Visual Studio.

if [[ -z ${LLVM_CONFIG} ]]; then
  LLVM_CONFIG=$(which llvm-config 2>/dev/null)
fi

RESULT=$(${LLVM_CONFIG} $1)

if [[ $1 == "--includedir" ]]; then
  # backslash -> slash
  RESULT=$(cygpath -am ${RESULT})
fi

echo ${RESULT}
