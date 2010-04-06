# NOTE
# - you can see the version from:
#   ftp://ftp.qlogic.com/outgoing/linux/firmware/CURRENT_VERSIONS
%define		driver ql2400
Summary:	Firmware for the QLogic %{driver} HBA
Summary(pl.UTF-8):	Firmware dla HBA QLogic %{driver}
Name:		%{driver}-firmware
Version:	5.03.02
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	ftp://ftp.qlogic.com/outgoing/linux/firmware/%{driver}_fw.bin
# Source0-md5:	f793a18130525f84f6c610c21b3fbba4
Source1:	ftp://ftp.qlogic.com/outgoing/linux/firmware/LICENSE
# Source1-md5:	4005328a134054f0fa077bdc37aa64f2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the QLogic %{driver} driver.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla sterownika QLogic %{driver}.

%prep
%setup -qcT
cp -a %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
/lib/firmware/*
