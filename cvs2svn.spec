%define		_documentid	42521

Summary:	CVS to Subversion or GIT Repository Converter
Summary(pl.UTF-8):	Konwerter repozytoriów CVS do Subversion lub GIT
Name:		cvs2svn
Version:	2.1.1
Release:	1
License:	Apache/BSD-like
Group:		Development/Version Control
Source0:	http://cvs2svn.tigris.org/files/documents/1462/%{_documentid}/%{name}-%{version}.tar.gz
# Source0-md5:	c1d5d97848658acdc293805b08e12959
URL:		http://cvs2svn.tigris.org/
BuildRequires:	python >= 1:2.5
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
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COMMITTERS README
%doc www
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/cvs2svn_rcsparse
%{py_sitescriptdir}/cvs2svn_lib
%{py_sitescriptdir}/*.egg-info
%{_mandir}/*/*
