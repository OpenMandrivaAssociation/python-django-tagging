%define realname django-tagging

Name:           python-django-tagging
Version:        0.3.1
Release:        %mkrel 2
Summary:        A generic tagging application for Django projects

Group:          Development/Python
License:        MIT
URL:            http://code.google.com/p/django-tagging/
# svn export -r154 http://django-tagging.googlecode.com/svn/trunk/ django-tagging-0.3-r154
# tar zcf django-tagging-0.3-r154.tar.gz django-tagging-0.3-r154
Source0:        http://django-tagging.googlecode.com/files/%{realname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-django

%description
A generic tagging application for Django projects, which allows association
of a number of tags with any Model instance and makes retrieval of tags
simple.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc CHANGELOG.txt LICENSE.txt README.txt docs/
%{py_puresitedir}/*
