%global tl_name hyphen-hebrew
%global tl_revision 74032

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Hebrew hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-hebrew
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-hebrew.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Prevents hyphenation in Arabic.

