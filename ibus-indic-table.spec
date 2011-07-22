Summary:	The Table engine for IBus platform
Name:		ibus-indic-table
Version:	1.3.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://fedorapeople.org/~nkumar/ibus-indic-table/ibus-indic-table-1.3.1/%{name}-%{version}.tar.gz
# Source0-md5:	9ed4e163b6a877193571943d62542b28
URL:		http://code.google.com/p/ibus/
Patch0:		%{name}-rhbz-683739.patch
Patch1:		%{name}-rhbz-703124.patch
BuildRequires:	ibus-devel
Requires:	ibus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Indic Table engine for IBus platform.

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
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/%{name}-createdb
%attr(755,root,root) %{_libexecdir}/ibus-engine-indic-table
%{_datadir}/ibus/component/indic-table.xml
%{_datadir}/%{name}
%{_npkgconfigdir}/%{name}.pc
