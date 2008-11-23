#
%define		nameprog ql2400

Summary:	Firmware for the QLogic %{nameprog} HBA
Summary(pl.UTF-8):	Firmware dla HBA QLogic %{nameprog}
Name:		%{nameprog}-firmware
Version:	4.04.05
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/%{nameprog}_fw.bin
# Source0-md5:	e6cc1a09f2b92fc91bfa57855cb647e2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the QLogic %{nameprog} driver.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla sterownika QLogic %{nameprog}.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/*
