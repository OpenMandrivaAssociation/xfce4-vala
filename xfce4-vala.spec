%define url_ver %(echo %{version} | cut -c 1-3)
%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:	Vala bindings for Xfce
Name:		xfce4-vala
Version:	4.10.3
Release:	1
License:	LGPLv2+
Group:		Development/Other
Url:		http://wiki.xfce.org/vala-bindings
Source0:	http://archive.xfce.org/src/bindings/xfce4-vala/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-dev-tools
BuildRequires:  pkgconfig(libvala-0.18)
BuildRequires:	vala
BuildRequires:	pkgconfig(exo-1)
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(libxfconf-0) >= 4.8.0
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
BuildRequires:	pkgconfig(libxfce4panel-1.0) >= 4.10

%description
Vala bindings for various Xfce components.

%prep
%setup -q

%build
%configure2_5x \
	--with-vala-api=0.24

%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/pkgconfig/xfce4-vala.pc
%{_datadir}/vala*/vapi/*.deps
%{_datadir}/vala*/vapi/*.vapi
