%global debug_package %{nil}

Name:           ctrl-app-dut
Version:        2.3.0
Release:        1%{?dist}
Summary:        Qualcomm WLAN control application for devices under test

License:        Qualcomm.nologin.binaries.license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260630.1/prebuilt_resolute/%{name}_%{version}_arm64.tar.gz

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
mkdir -p %{buildroot}
cp -a data/%{name}/arm64/. %{buildroot}/
# Install license documents separately with %license.
rm -f %{buildroot}%{_docdir}/%{name}/copyright
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files
%license data/%{name}/arm64/usr/share/doc/%{name}/copyright

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 2.3.0-1
- Initial prebuilt RPM packaging
