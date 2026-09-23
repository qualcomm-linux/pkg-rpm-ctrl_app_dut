%global debug_package %{nil}
%global source_version 1.0

Name:           ctrl-app-dut
Version:        2.3.0
Release:        1%{?dist}
Summary:        Qualcomm WLAN control application for devices under test

License:        Qualcomm.nologin.binaries.license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260825/prebuilt_yocto/qcom-%{name}_%{source_version}_armv8-2a.tar.gz

ExclusiveArch:  aarch64

%description
ctrl-app-dut provides device-side control for testing Qualcomm WLAN
devices. It runs on the device under test (DUT) and allows a test
controller to configure the device and perform WLAN test operations.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}%{_bindir}
cp -a usr %{buildroot}/
ln -s ../sbin/ctrl_app_dut %{buildroot}%{_bindir}/ctrl_app_dut
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files
%license usr/share/doc/qcom-%{name}/NO.LOGIN.BINARY.LICENSE.QTI
%license usr/share/doc/qcom-%{name}/LICENSE

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 2.3.0-1
- Initial prebuilt RPM packaging
