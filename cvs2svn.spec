Summary:	CVS to Subversion Repository Converter
Summary(pl):	Konwerter repozytoriów CVS do Subversion
Name:		cvs2svn
Version:	1.1.0
Release:	2
License:	Apache/BSD-like
Group:		Development/Version Control
Source0:	http://cvs2svn.tigris.org/files/documents/1462/16792/%{name}-%{version}.tar.gz
# Source0-md5:	8e273e69123872f0ff55ade7cff8e7c8
URL:		http://cvs2svn.tigris.org/
BuildRequires:	python
%pyrequires_eq	python-libs
Requires:	python-subversion >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS to Subversion Repository Converter.

%description -l pl
Konwerter repozytoriów CVS do Subversion.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COMMITTERS README design-notes.txt
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/cvs2svn_rcsparse
%{py_sitescriptdir}/cvs2svn_rcsparse/*.*[co]
