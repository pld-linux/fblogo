Summary:	Create your own fblogo shown on system start
Summary(pl):	Narzêdzie do tworzenia w³asnego logo wy¶wietlanego podczas startu systemu
Name:		fblogo
Version:	0.5.0
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://freakzone.net/gordon/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://freakzone.net/gordon/
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags} -Wall -DPNG_SETJMP_NOT_SUPPORTED"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc CHANGES README
%{_bindir}/fblogo*
%{_mandir}/man1/fblogo*.1*
