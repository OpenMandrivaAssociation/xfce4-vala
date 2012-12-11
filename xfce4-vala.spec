%define url_ver %(echo %{version} | cut -c 1-3)
%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:	Vala bindings for Xfce
Name:		xfce4-vala
Version:	4.8.1
Release:	1
License:	LGPLv2+
Group:		Development/Other
Url:		http://wiki.xfce.org/vala-bindings
Source0:	http://archive.xfce.org/src/bindings/xfce4-vala/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		xfce4-vala-4.8.1-rosa-vala018.patch
BuildRequires:	xfce4-dev-tools
BuildRequires:  pkgconfig(libvala-0.18)
BuildRequires:	vala
BuildRequires:	exo-devel
BuildRequires:	pkgconfig(libxfconf-0) >= 4.8.0
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.8.0

%description
Vala bindings for various Xfce components.

%prep
%setup -q
%patch0 -p1

%build
xdt-autogen
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/pkgconfig/xfce4-vala.pc
%{_datadir}/vala*/vapi/*.deps
%{_datadir}/vala*/vapi/*.vapi


%changelog
* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2011.0
+ Revision: 633060
- rebuild for new Xfce 4.8.0

* Sun Oct 31 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2011.0
+ Revision: 591134
- update to new version 4.6.1
- fix buildrequires
- import xfce4-vala


