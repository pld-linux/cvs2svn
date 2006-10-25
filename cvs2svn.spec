%define		_documentid	34574

Summary:	CVS to Subversion Repository Converter
Summary(pl):	Konwerter repozytoriów CVS do Subversion
Name:		cvs2svn
Version:	1.5.0
Release:	1
License:	Apache/BSD-like
Group:		Development/Version Control
Source0:	http://cvs2svn.tigris.org/files/documents/1462/%{_documentid}/%{name}-%{version}.tar.gz
# Source0-md5:	dc5bf68303498542cfa061f7ae79d9dd
URL:		http://cvs2svn.tigris.org/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	rcs
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
%doc BUGS COMMITTERS README design-notes.txt
%doc www
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/cvs2svn_rcsparse
%{py_sitescriptdir}/cvs2svn_lib
%{_mandir}/*/*
