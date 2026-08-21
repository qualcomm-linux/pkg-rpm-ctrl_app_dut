<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# ctrl-app-dut RPM - CentOS Stream 10

This branch contains the CentOS Stream 10 RPM packaging for ctrl-app-dut from a prebuilt payload tarball.

## Package

| Field | Value |
|---|---|
| Package | ctrl-app-dut |
| Version | 2.3.0 |
| Source | ctrl-app-dut-prebuilt-2.3.0.tar.gz |
| Source checksum | See sources |

The prebuilt payload installs:

- /usr/bin/ctrl_app_dut
- /usr/sbin/ctrl_app_dut

## Files

- ctrl-app-dut.spec
- sources
- .github/workflows/build-on-pr.yml
- .github/workflows/pkg-release.yml

Do not commit source tarballs or built RPMs. This package uses a prebuilt payload tarball, so the tarball must be available in the lookaside cache before CI can build it.

## Build

Local validation can be run with qcom-rpm-utils:

    /path/to/qcom-rpm-utils/scripts/build-rpm.sh \
      --tarball /path/to/ctrl-app-dut-prebuilt-2.3.0.tar.gz \
      --spec ctrl-app-dut.spec \
      --output /path/to/output

For CI, open a PR against this c10s branch. The build-on-pr workflow builds RPM artifacts but does not publish them.

## Release

After the PR is merged, run Actions -> Release on the c10s branch. The release workflow publishes the generated RPMs to Artifactory after approval.
