%define	name	SDL_ttf
%define	version	2.0.9
%define	release	%mkrel 1
%define	lib_name_orig	lib%{name}
%define	lib_major	2.0
%define	lib_name	%mklibname %{name} %{lib_major}

Summary:	Simple DirectMedia Layer - Sample TrueType Font Library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.bz2
Patch0:		SDL_ttf-2.0.8-noftinternals.patch
Patch1:         SDL_ttf-2.0.8-fix-mono-bitmaps-returned-when-nonmono-was-expected.patch
License:	LGPL
URL:		http://www.libsdl.org/projects/SDL_ttf/
Group:		System/Libraries
BuildRequires:	SDL-devel X11-devel audiofile-devel esound-devel freetype2-devel >= 2.1.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a sample library which allows you to use TrueType fonts in your SDL
applications. It comes with an example program "showfont" which displays an
example string for a given TrueType font file.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n	%{lib_name}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n	%{lib_name}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel

%description -n	%{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n	%{lib_name}-test
Summary:	Test binary for %{name}
Group:		System/Libraries

%description -n	%{lib_name}-test
This package contains binary to test the associated library.

%prep
%setup -q
#patch0 -p1 -b .noftinternals
#%patch1 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 .libs/{showfont,glfont} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}-test
%defattr(-,root,root)
%{_bindir}/showfont
%{_bindir}/glfont

%files -n %{lib_name}
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/lib*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc README COPYING CHANGES
%{_libdir}/*a
%{_libdir}/lib*.so
%{_includedir}/SDL/*


