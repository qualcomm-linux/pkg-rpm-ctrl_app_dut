%global debug_package %{nil}

Name:           ctrl-app-dut
Version:        2.3.0
Release:        1%{?dist}
Summary:        Qualcomm WLAN control application DUT binary

License:        Qualcomm.nologin.binaries.license
URL:            https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260630.1/prebuilt_resolute/%{name}_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
ctrl-app-dut is a prebuilt Qualcomm WLAN DUT control application for
Qualcomm Linux platforms.

%prep
%autosetup -n data

%build
# Prebuilt binaries -- no compilation required.

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_docdir}/%{name}

install -m 0755 %{name}/arm64/usr/sbin/ctrl_app_dut \
    %{buildroot}%{_sbindir}/ctrl_app_dut
ln -s ../sbin/ctrl_app_dut %{buildroot}%{_bindir}/ctrl_app_dut
install -m 0644 %{name}/arm64/usr/share/doc/%{name}/copyright \
    %{buildroot}%{_docdir}/%{name}/copyright
install -m 0644 %{name}/arm64/usr/share/doc/%{name}/changelog.gz \
    %{buildroot}%{_docdir}/%{name}/changelog.gz

%files
%license %{_docdir}/%{name}/copyright
%doc %{_docdir}/%{name}/changelog.gz
%{_bindir}/ctrl_app_dut
%{_sbindir}/ctrl_app_dut

%changelog
* Fri Aug 14 2026 Yu Zhang <yuzha@qti.qualcomm.com> - 2.3.0-1
- Initial RPM packaging of ctrl-app-dut prebuilt binary
