Summary:	Create your own fblogo showed on system start
Summary(pl):	Narzêdzie do tworzenia w³asnego logo wy¶wietlanego podczas startu systemu
Name:		fblogo
Version:	0.5.0
Release:	1
URL:		http://freakzone.net/gordon
License:	GPL
Group:		Applications/Console
Source0:	http://freakzone.net/gordon/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libpng

%description
With this program, you can convert your favourite image to framebuffer
logo, which you can apply to your kernel sources then. 

%description -l pl
Korzystaj±c z tego programu, mo¿na przekszta³ciæ ulubiony obrazek na
logo framebuffera.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}/%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
%{__make} install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%{_bindir}/fblogo*
%{_mandir}/man1/fblogo*.1*
