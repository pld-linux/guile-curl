Summary:	URL-fetching library for Guile
Summary(pl.UTF-8):	Biblioteka pobierania URL-i dla Guile
Name:		guile-curl
Version:	0.9
Release:	1
License:	GPL v3+
Group:		Libraries
#Source0Download: https://github.com/spk121/guile-curl/releases
Source0:	https://github.com/spk121/guile-curl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1dee446b9c0cb62aa415d57dfb3a8439
Patch0:		%{name}-info.patch
URL:		https://github.com/spk121/guile-curl
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	guile-devel >= 5:2.2
BuildRequires:	guile-devel < 5:3.2
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Requires:	guile-libs >= 5:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guile-curl is a project that has procedures that allow Guile to do
client-side URL transfers, like requesting documents from HTTP or FTP
servers. It is based on the libcurl library.

%description -l pl.UTF-8
guile-curl to projekt zawierający procedury pozwalające na wykonywanie
z poziomu Guile klienckich transferów URL-i, np. żadanie dokumentów z
serwerów HTTP lub FTP. Jest oparty na bibliotece libcurl.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/3.0/extensions/*.la

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}/*.scm $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/guile/3.0/extensions/libguile-curl.so*
%{_libdir}/guile/3.0/site-ccache/curl.go
%{_datadir}/guile/site/3.0/curl.scm
%{_infodir}/guile-curl.info*
%{_examplesdir}/%{name}-%{version}
