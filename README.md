<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# ctrl-app-dut RPM - CentOS Stream 10

ctrl-app-dut provides device-side control for testing Qualcomm WLAN
devices. It runs on the device under test (DUT) and allows a test
controller to configure the device and perform WLAN test operations.

This branch contains the CentOS Stream 10 RPM packaging for ctrl-app-dut from a Qualcomm Linux release tarball.

## Package

| Field | Value |
|---|---|
| Package | ctrl-app-dut |
| Summary | Qualcomm WLAN control application for devices under test |
| Version | 2.3.0 |
| Source | ctrl-app-dut_2.3.0_arm64.tar.gz |
| Source checksum | See sources |

The prebuilt payload installs:

- /usr/bin/ctrl_app_dut
- /usr/sbin/ctrl_app_dut

License documents are installed under `/usr/share/licenses/ctrl-app-dut/`
and marked as license files in the RPM:

- `copyright`

## Files

- ctrl-app-dut.spec
- sources
- .github/workflows/build-on-pr.yml
- .github/workflows/pkg-release.yml

Do not commit source tarballs or built RPMs. The source tarball is resolved from the dist-git `sources` file and the spec `Source0` URL.

## Build

Local validation can be run with qcom-rpm-utils:

    /path/to/qcom-rpm-utils/scripts/build-rpm.sh \
      --tarball /path/to/ctrl-app-dut_2.3.0_arm64.tar.gz \
      --spec ctrl-app-dut.spec \
      --output /path/to/output

For CI, open a PR against this c10s branch. The build-on-pr workflow builds RPM artifacts but does not publish them.

## Release

After the PR is merged, run Actions -> Release on the c10s branch. The release workflow publishes the generated RPMs to Artifactory after approval.
