# Trivial test for importing XCTest.
#

# This test doesn't work on Darwin yet, because the XCTest overlay isn't shipped
# with the package, and can't be found:#
#   <rdar://problem/23600043> Cannot import XCTest with swift from a downloadable package
# REQUIRES: platform=Linux
#
# Make a sandbox dir.
# RUN: rm -rf %t.dir
# RUN: mkdir -p %t.dir/tool
# RUN: touch %t.dir/tool/Package.swift
# RUN: cp %S/main.swift %t.dir/tool/main.swift
# RUN: %{swift} build --chdir %t.dir/tool -v > %t.build-log

# Check the build log.
#
# RUN: %{FileCheck} --check-prefix CHECK-BUILD-LOG --input-file %t.build-log %s
#
# CHECK-BUILD-LOG: swiftc{{.*}} -module-name tool

# Verify that the tool exists and works.
#
# RUN: test -x %t.dir/tool/.build/debug/tool
# RUN: %t.dir/tool/.build/debug/tool > %t.out
# RUN: %{FileCheck} --check-prefix CHECK-TOOL-OUTPUT --input-file %t.out %s
#
# CHECK-TOOL-OUTPUT: HI
