%define		documentid	46528
%define		subver		r15319
%define		rel		1
Summary:	CVS to Subversion or GIT Repository Converter
Summary(pl.UTF-8):	Konwerter repozytoriów CVS do Subversion lub GIT
Name:		cvs2svn
Version:	2.3.0
Release:	3.%{subver}.%{rel}
License:	Apache/BSD-like
Group:		Development/Version Control
Source0:	%{name}-r15319.tar.bz2
# Source0-md5:	f3de6d9ed0673b9de173e51e1912763b
URL:		http://cvs2svn.tigris.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	rcs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS to Subversion or GIT Repository Converter.

%description -l pl.UTF-8
Konwerter repozytoriów CVS do Subversion lub GIT.

%prep
%setup -q -n %{name}-trunk

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
%py_install

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COMMITTERS README
%doc www
%attr(755,root,root) %{_bindir}/cvs2bzr
%attr(755,root,root) %{_bindir}/cvs2git
%attr(755,root,root) %{_bindir}/cvs2svn
%{py_sitescriptdir}/cvs2svn_rcsparse
%{py_sitescriptdir}/cvs2svn_lib
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
