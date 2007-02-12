Summary:	Create your own fblogo shown on system start
Summary(pl.UTF-8):	Narzędzie do tworzenia własnego logo wyświetlanego podczas startu systemu
Name:		fblogo
Version:	0.5.2
Release:	2
License:	GPL
Group:		Applications/Console
Source0:	http://freakzone.net/gordon/src/%{name}-%{version}.tar.gz
# Source0-md5:	f60cb2a3378bb392c86ea6e4f8006cc0
Patch0:		%{name}-Makefile.patch
URL:		http://freakzone.net/gordon/
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this program, you can convert your favourite image to framebuffer
logo, which you can apply to your kernel sources then.

%description -l pl.UTF-8
Korzystając z tego programu, można przekształcić ulubiony obrazek na
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/fblogo*
%{_mandir}/man1/fblogo*.1*
