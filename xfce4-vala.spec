%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Vala bindings for Xfce
Name:		xfce4-vala
Version:	4.6.0
Release:	%mkrel 1
License:	LGPLv2+
Group:		Development/Other
Url:		http://wiki.xfce.org/vala-bindings
Source0:	http://archive.xfce.org/src/bindings/xfce4-vala/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:  vala-devel
BuildRequires:	exo-devel
BuildRequires:	xfce4panel-devel
BuildRequires:	libxfce4menu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Vala bindings for various Xfce components.

%prep
%setup -q %{name}-%{version}

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/pkgconfig/xfce4-vala.pc
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
