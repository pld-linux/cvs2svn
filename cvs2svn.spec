Summary:	CVS to Subversion Repository Converter
Summary(pl):	Konwerter repozytoriów CVS do Subversion
Name:		cvs2svn
Version:	1.0.0
Release:	1
License:	Apache/BSD-like
Group:		Development/Version Control
Source0:	http://cvs2svn.tigris.org/files/documents/1462/15996/%{name}-%{version}.tar.gz
# Source0-md5:	10bf79f793db14a2e2fb3670336c5e2a
URL:		http://cvs2svn.tigris.org/
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
