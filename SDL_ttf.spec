%define	lib_name_orig	lib%{name}
%define	major 0
%define	apiver 2.0
%define	libname %mklibname %{name} %{apiver} %{major}
%define	develname %mklibname -d %{name}

Summary:	Simple DirectMedia Layer - Sample TrueType Font Library
Name:		SDL_ttf
Version:	2.0.11
Release:	7
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.libsdl.org/projects/SDL_ttf/
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(freetype2)

%description
This is a sample library which allows you to use TrueType fonts in your SDL
applications. It comes with an example program "showfont" which displays an
example string for a given TrueType font file.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n %{libname}-test
Summary:	Test binary for %{name}
Group:		System/Libraries
Conflicts:	showfont

%description -n	%{libname}-test
This package contains binary to test the associated library.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -lm"
%configure2_5x --disable-static
%make

%install
%makeinstall_std
%__install -d %{buildroot}%{_bindir}
%__install -m755 .libs/{showfont,glfont} %{buildroot}%{_bindir}

%files -n %{libname}-test
%{_bindir}/showfont
%{_bindir}/glfont

%files -n %{libname}
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%doc README CHANGES
%{_libdir}/lib*.so
%{_includedir}/SDL/*
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Mar 19 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0.11-1mdv2012.0
+ Revision: 785485
- New version 2.0.11

* Mon Dec 19 2011 Andrey Bondrov <abondrov@mandriva.org> 2.0.10-3
+ Revision: 743798
- Rebuild to remove .la files

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.10-2
+ Revision: 671973
- mass rebuild

* Sun Aug 15 2010 Emmanuel Andry <eandry@mandriva.org> 2.0.10-1mdv2011.0
+ Revision: 570173
- New version 2.0.10
- update files list

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.9-6mdv2010.0
+ Revision: 413012
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.0.9-5mdv2009.0
+ Revision: 265684
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 29 2008 Funda Wang <fwang@mandriva.org> 2.0.9-4mdv2009.0
+ Revision: 213043
- manually -lm
- obsoletes correct libname

* Wed Jan 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.9-3mdv2008.1
+ Revision: 153635
- obsolete older library and test subpackage

* Tue Jan 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.9-2mdv
+ Revision: 151991
- new license policy
- fix mixture of spaces and tabs
- spec file clean
- do not package COPYING file

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - add explicit conflict with showfont package

* Sun Jul 22 2007 Funda Wang <fwang@mandriva.org> 2.0.9-1mdv2008.0
+ Revision: 54384
- New develpackage policy
- New version

* Wed Jun 06 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.0.8-5mdv2008.0
+ Revision: 36090
- Rebuild with libslang2.

* Sat May 26 2007 Funda Wang <fwang@mandriva.org> 2.0.8-4mdv2008.0
+ Revision: 31379
- rebuild agasinst directfb 1.0


* Sat Feb 24 2007 Giuseppe Ghibò <ghibo@mandriva.com> 2.0.8-3mdv2007.0
+ Revision: 125392
- Rebuilt against latest libgii/libggi
- Import SDL_ttf

* Tue Aug 29 2006 Guillaume Cottenceau 2.0.8-2mdk2007.0
- author patch1 to fix a bug when a mono bitmap is returned
  when a non mono was expected (submitted upstream, but a
  debian guy said SDL stuff usually take a long time for
  a new release)

* Wed Jun 07 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.8-1mdv2007.0
- 2.0.8
- fix build against new freetype (P0)
- %%mkrel
- cosmetics

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.0.7-2mdk
- Rebuild

* Wed Mar 23 2005 Giuseppe Ghibò <ghibo@mandrakesoft.coM> 2.0.7-1mdk
- Release: 2.0.7.

* Wed Mar 23 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 2.0.6-5mdk
- Rebuilt.

