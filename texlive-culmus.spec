%global tl_name culmus
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Hebrew fonts from the Culmus project
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/culmus
License:	lppl1.3 gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/culmus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/culmus.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/culmus.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hebrew fonts from the Culmus Project. Both Type1 and Open/TrueType
versions of the fonts are provided, as well as font definition files. It
is recommended to use these fonts with the NHE8 font encoding, from the
hebrew-fonts package.

