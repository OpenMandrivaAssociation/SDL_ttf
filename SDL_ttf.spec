%define	lib_name_orig	lib%{name}
%define	major 0
%define apiver 2.0
%define	libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname -d %{name}

Summary:	Simple DirectMedia Layer - Sample TrueType Font Library
Name:		SDL_ttf
Version:	2.0.10
Release:	%mkrel 3
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.libsdl.org/projects/SDL_ttf/
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel
BuildRequires:	freetype2-devel >= 2.1.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Obsoletes:	%mklibname %{name} 2.0

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
Obsoletes:	%mklibname %{name} 2.0 -d

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
Obsoletes:	%{mklibname %{name} 2.0}-test

%description -n	%{libname}-test
This package contains binary to test the associated library.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -lm"
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -d %{buildroot}%{_bindir}
install -m755 .libs/{showfont,glfont} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}-test
%defattr(-,root,root)
%{_bindir}/showfont
%{_bindir}/glfont

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README CHANGES
%{_libdir}/*a
%{_libdir}/lib*.so
%{_includedir}/SDL/*
%{_libdir}/pkgconfig/*.pc
