Summary:	The Indic Table engine for IBus platform
Summary(pl.UTF-8):	Silnik Indic Table dla platformy IBus
Name:		ibus-indic-table
Version:	1.3.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://fedorapeople.org/~nkumar/ibus-indic-table/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9ed4e163b6a877193571943d62542b28
Patch0:		%{name}-rhbz-683739.patch
Patch1:		%{name}-rhbz-703124.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	gettext-devel >= 0.16.1
BuildRequires:	ibus-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
Requires:	ibus >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Indic Table engine for IBus platform.

%description -l pl.UTF-8
Silnik Indic Table dla platformy IBus.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-additional

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_npkgconfigdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}-createdb
%attr(755,root,root) %{_libexecdir}/ibus-engine-indic-table
%{_datadir}/ibus/component/indic-table.xml
%{_datadir}/%{name}
%{_npkgconfigdir}/%{name}.pc
