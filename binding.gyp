{
  "variables": {
    # On Windows, this command is executed in cmd.exe, where "./" is illegal,
    # but $PATH remains so that "bash" of MSYS still works.
    "llvm_config": "<!(bash llvm-config.sh)",
  },
  "targets": [
    {
      "target_name": "clang",
      "sources": [
        "src/clang_translationunit.cpp",
        "src/clang.cpp",
        "src/clang_helpers.cpp",
        "src/command_line_args.cpp",
        "src/completion.cpp",
        "src/diagnostic.cpp",
        "src/unsaved_files.cpp",
      ],
      "defines": [
        "__STDC_CONSTANT_MACROS",
        "__STDC_FORMAT_MACROS",
        "__STDC_LIMIT_MACROS",
      ],
      "cflags!": [
      ],
      "cflags_cc!": [
      ],
      "cflags": [
        "-g",
        "-O2",
      ],
      "cflags_cc": [
        "-g",
        "-std=c++11",
        "-O2",
      ],
      "ldflags": [
        "-flto",
      ],
      "xcode_settings": {
        "GCC_GENERATE_DEBUGGING_SYMBOLS": "YES",
        "CLANG_CXX_LANGUAGE_STANDARD": "c++11",
        "GCC_OPTIMIZATION_LEVEL": "2",
        "OTHER_CFLAGS": [
        ],
        "OTHER_LDFLAGS": [
        ],
      },
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "link_settings": {
        "conditions": [
          ["OS!='win'", {
            "libraries": [
              "-Wl,-rpath,<!(<(llvm_config) --libdir)",
              "<!@(<(llvm_config) --ldflags)",
              "-lclang",
              "<!@(<(llvm_config) --system-libs)",
            ]
          }]
        ]
      },
      "msvs_settings": {
        "VCLinkerTool": {
          "AdditionalLibraryDirectories": [
            "<!(<(llvm_config) --libdir)"
          ],
          "AdditionalDependencies": [
            "libclang.dll.a",
            "psapi.lib"
          ]
        }
      },
      "conditions": [
        ["OS!='win'", {
          "include_dirs": [
            "<!@(<(llvm_config) --includedir)"
          ],
          "defines": [
            "CLANG_SEARCH_PATH=\"<!(<(llvm_config) --libdir)/clang/<!(<(llvm_config) --version)/include\""
          ]
        }],
        ["OS=='win'", {
          "include_dirs": [
            "<!@(cygpath -am <!(<(llvm_config) --includedir))"
          ],
          "defines": [
            "CLANG_SEARCH_PATH=\"<!(cygpath -am <!(<(llvm_config) --libdir))/clang/<!(<(llvm_config) --version)/include\""
          ]
        }],
      ],
    },
  ]
}
